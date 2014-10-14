Title: Data Science Incubator, Week 2
Date: 2014-10-09
Category: daily
Tags: becker, kbmod, incubator, brandon, grappa

I spent today in the Data Science Incubator working with [Andy Becker](http://www.astro.washington.edu/users/becker/) on [KBMOD](https://github.com/uwescience/kbmod). We are trying to port the key components of the moving object detection into PostgreSQL using PostGIS.

On his own, Andy designed a schema for the various data, including spatial columns and indexes. Side by side, we worked on a few issues:

* Speeding up data load: `\COPY` is much faster than large batch insert statements, as we know.
* Explaining queries and seeing whether indexes are used: not yet, but the database is small so sequential scans might actually make more sense. Also, it looks like the optimizer may miss some tricks in some cases.
* Cloud-ification: we set up an Amazon RDS PostgreSQL+PostGIS database, and proved that we could load data in, even large data.
* Astro UDFs: for the kinds of spatial queries that we need, there are great C++ libraries that do all the work; we need access to those UDFs in the database! We [began investigating](https://github.com/uwescience/kbmod/issues/1) PostgreSQL support for UDFs as compiled C binaries; this should be doable, but we may need to fiddle to make the C++ code play nice with PostgreSQL, which expects C...
* UDFs may be a show-stopper for using RDS, however -- you cannot register binary UDFs there, so we will likely have to kill the RDS instance and setup a manually managed EC2+PostgreSQL instance instead.

    Aside: Automatically-managed cloud services are *very* appealing, but little implementation issues like this always seem to bite us. Similar limitations apply to Microsoft SQL Azure [no stored procedures], and Google App Engine [no CPython]---our needs always push us into the "Sorry, you have to do *everything* manually now" use case, or make us dramatically restrict the performance and capabilities of our applications. Surely this issue crops up for other users!
    
For next week, some preliminary goals are:

* move from RDS to EC2
* get a bigger dataset into the database, so we are in a real optimization framework
* get the UDF into the database
* work on expressing the queries and testing correctness
* optimize the indexes and queries

We also chatted with [Brandon Holt](http://homes.cs.washington.edu/~bholt/), [Brandon Myers](http://r.halper.in/coauth/bdmyers), and Simon Kahan about possible [Grappa](http://grappa.io/)--KBMOD connections.