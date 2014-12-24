Title: Myria updates
Date: 2014-12-23
Category: daily
Tags: dominik, jingjing, shumo, myria

Not much happening this week, what with the holidays. I took advantage of the break to handle some long-overdue code reviews and code improvements to Myria.

* [Jingjing Wang](http://r.halper.in/coauth/jwang) has added resource profiling to Myria. We can now measure the resource consumption of each operator during query execution. (Unfortunately, these data are not yet available from the website.) See [myria#656](https://github.com/uwescience/myria/pull/656) and [myria-web#241](https://github.com/uwescience/myria-web/pull/241).

* [Dominik Moritz](http://r.halper.in/coauth/domoritz) implemented binary copy for Postgres. Database inserts are now substantially faster, especially for floating point or doubles where we could not use the `COPY` mode before (turns out `double` → `string` → `double` is not an identity-preserving transform. Duh.) See [myria#667](https://github.com/uwescience/myria/pull/667) and [myria#669](https://github.com/uwescience/myria/pull/669).

    Dominik also improved the performance of the profiler using the new interface. [myria#672](https://github.com/uwescience/myria/pull/672)

* [Shumo Chu](http://r.halper.in/coauth/chushumo) is getting Myria ready for Apache licensing -- we just need to get rid of a few pesky GPL'ed dependencies. Tentatively, it looks like we have easy switch-in replacements that might also yield a bit faster query execution. [myria#658](https://github.com/uwescience/myria/pull/658)

* I upgraded our continuous integration to Travis-CI's new Docker-based containers. This lets us re-enable caching and also tests that execute multicore and faster! [myria#673](https://github.com/uwescience/myria/pull/673) and [myria#674](https://github.com/uwescience/myria/pull/674).

* As part of these upgrades I cleaned up and better tested several operators.

In short: nothing much to see here, but Myria will hopefully work faster and better. One of Sophie's sample queries [sped up from 12m to 4m](https://demo.myria.cs.washington.edu/queries?q=good_files_v4_profiled+%3D+0&max=59793&limit=2), and the 3x improvement is entirely due to the binary inserts!

We have also begun interviewing candidates for the Myria software engineer position.