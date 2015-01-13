Title: Intro to SQLShare
Date: 2015-01-06
Category: daily
Tags: dacb, sr320, talks, sqlshare

[David Beck](http://faculty.washington.edu/dacb/) asked me somewhat last-minute to open this quarter's [IGERT](http://escience.washington.edu/education/IGERT/overview) [Community Seminar](http://escience.washington.edu/community_seminar) with a half-hour discussion of [SQLShare](http://escience.washington.edu/sqlshare). I dusted off the slides from the [What to teach Biologists about Computing? (w2tbac)'13](https://storify.com/ctitusbrown/what-to-teach-biologists-about-computing) meeting. (Slides [here](http://www.slideshare.net/dhalperi/a-24064276).) My goal was to give the room (mostly Ph.D. students and postdocs from science departments on campus) an intuition about what SQL is and why we think it is useful. Dave, of course, has had great success using SQL in his work and that is why he asked me to talk.

[Steven Roberts](http://faculty.washington.edu/sr320/?cat=44) -- Associate Professor in Aquatic & Fisheries Science -- gave the second half of the seminar. Steven is a campus leader in open science, and he and his lab have been some of our best SQLShare users. Steven talked about how his lab uses SQLShare to analyze data, manage data, automate standardized processing, and how it integrates into their standard IPython processing pipelines. Steven also presented his students' real queries of varying complexity and application, and he discussed how he uses SQLShare when teaching.

The video of Steven's talk may be posted soon at the [Community Seminar website](http://escience.washington.edu/community_seminar).

During Steven's talk, I observed that both the breadth and depth of the queries he presented far exceeded the queries we directly showed them as examples. This is a sign of success -- the students autonomously authored significantly more complex queries!

Unfortunately, some of the queries had issues: some stylistic issues that might lead to very slow database performance (not a big deal, but inconvenient), and at least one correctness bug (a `where a-b < abs(0.2)` -- the `abs` needs to be around the `a-b`). [In this case, the buggy code was actually replaced with a different tool, so it thankfully had no affect on the science.]

I wonder how we can better add code review or sanity checking into the teaching and adoption process for our data science tools. There are at least two fruitful directions:

1. query editor that recognizes snippets that don't make sense and offers suggestions. We could recommend the query author replace `a LIKE 'bc'` with `a = 'bc'` and warn on `abs(0.2)` because `abs` applied to a constant can always be simplified.
2. code review of important queries. Most of these SQL queries, when paired with an English statement of intent, can be vetted fairly quickly. But we need to think hard about the time, resources, and process around such a review.