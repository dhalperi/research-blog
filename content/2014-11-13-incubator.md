Title: Incubator 7.2
Date: 2014-11-13
Category: daily
Tags: becker, kbmod, incubator

More work with [Andy Becker](http://www.astro.washington.edu/users/becker/)  on the KBMOD database and query design today. We have been running into issues loading all the pixels in the database -- O(Millions) of images with O(Millions) of pixels each means 10^12 records, which would take years to load into our Postgres database. A parallel database like Greenplum, or Myria, would speed up the load linearly but this may not help much.

An alternate tack is to rethink our queries: rather than one record per pixel, one record per image and then a user-defined function to dereference the pixel in an image when needed. We talked about how we might structure the tables and queries to accomplish this design and ended up with a relatively simple workflow:

1. a *trajectory* becomes a list of bounding boxes, one for each run [night] in which we measured the sky. This bounding box roughly corresponds to [(`ra0`, `dec0`), (`ra1`, `dec1`)], which are the positions of the TNO at times `t0` and `t1` corresponding to the beginning and end of the run.
2. we intersect the per-run trajectory bounding boxes with the bounding box for each image during that run to determine which images might have overlapped with the trajectory.
3. we compute the position of the TNO at the acquisition time of each image to determine whether the TNO was was actually in the image at all and, if so, in which precise pixel it was captured.
4. we co-add all the pixels.

My guess is that we end up keeping steps 1 & 2 in the database, but 3 & 4 are performed outside the database in custom code. Since the images themselves represent the majority of the data, we'll want to read each image into memory at most once while fetching the desired pixels for many trajectories. Obviously we will try many approaches, but my guess is that we will have better control over this performance-critical code outside of the database.

For more information, see the KBMOD discussion on GitHub: <https://github.com/uwescience/kbmod/issues/3>