Title: Incubator week 3.1
Date: 2014-10-14
Category: daily
Tags: becker, sophie, incubator, seaflow, kbmod, sqlshare

Today was day 1 of [Incubator](http://data.uw.edu/incubator) week 3.

[Sophie Clayton](http://r.halper.in/coauth/sclayton) exposed a locking issue in [SQLShare](http://sqlshare.escience.washington.edu): if a running query reads from table `T` and a user changes the sharing on table `T`, SQLShare basically locks the entire system until the query finishes. We need to revisit this issue, but it is unlikely to be a common problem: today was literally the first time it has ever cropped up. We also discussed a variety of SQL-isms such as how to convert a Julian Day into a `Date` and the like. Sophie is now really off to the races with the underway data.

[Andy Becker](http://r.halper.in/people/becker) and I played with various methods of inspecting on the progress and performance of his loading data into PostgreSQL. We went down a bit of a rabbit-hole when trying to figure out why it was not using the index to compute the number of distinct fields in the database:

```sql
kbmod=> explain select count(*) from (select distinct fieldid from pixels) X;
                                   QUERY PLAN
---------------------------------------------------------------------------------
 Aggregate  (cost=19138399.42..19138399.43 rows=1 width=0)
   ->  HashAggregate  (cost=19138399.40..19138399.41 rows=1 width=8)
         ->  Seq Scan on pixels  (cost=0.00..17631684.52 rows=602685952 width=8)
(3 rows)

Time: 9.729 ms


kbmod=> \d pixels;
                                   Table "public.pixels"
 Column  |         Type         | Modifiers
---------+----------------------+----------------------------------------------------------
 pixelid | bigint               | not null default nextval('pixels_pixelid_seq'::regclass)
 fieldid | bigint               | not null
 ra      | double precision     |
 decl    | double precision     |
 fval    | real                 |
 radec   | geometry(Point,3786) |
 mask    | integer              |
Indexes:
    "pixels_pkey" PRIMARY KEY, btree (pixelid)
    "fieldidx" btree (fieldid)
Foreign-key constraints:
    "pixels_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES fields(fieldid)
```
As it turns out, PostgreSQL's `DISTINCT` implementation simply cannot do the right thing.

I also set up the [Incubator Blog](http://uwdatascienceincubator.wordpress.com/) today: it combines posts from all of the incubator participants. Setting up this blog was really cool -- I used [If This, Then That (IFTTT)](https://ifttt.com/) to automatically crawl the feeds from the individual blogs and post them on a shared Wordpress! (Thanks to our friends at UC Berkeley for recommending IFTTT via the new Slack communication channel we've all been using.)