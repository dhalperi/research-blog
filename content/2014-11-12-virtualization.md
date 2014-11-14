Title: Public cluster + private experiments
Date: 2014-11-12
Category: posts
Tags: myria

The hot button issue today is what we do with our public Myria service.

As part of the grant proposal, we promised that "the project develops and deploys a Web-based query-as-a-service interface to the new middleware. The service will be made available to domain scientists" (p.1). This service has been working gangbusters:

- I have written before about the [MyMergerTree](http://r.halper.in/paper/Loebman_MergerTree_2014.pdf) service built by students and faculty in the UW Database and Astronomy groups, led by [Magda Balazinska](http://r.halper.in/coauth/magda) and [Sarah Loebman](http://r.halper.in/coauth/loebman) on the faculty side. MyMergerTree is just awesome and used by researchers in Astronomy still.
- [Sophie Clayton](http://r.halper.in/coauth/sclayton)'s [Incubator project](https://github.com/uwescience/incubator/wiki/Patterns-in-phytoplankton-diversity) uses Myria to analyze large (tens of cruises, thousands of hours, billions of cells) oceanographic data. Among Myria users, Sophie is the one really innovating at combining Myria with other tools, such as her [IPython notebooks](https://github.com/uwescience/seaflow-myria/tree/master/ipython_notebooks).
- [Brandon Myers](http://r.halper.in/coauth/bdmyers) and York Wei have been working on [abstracting the Myria web frontend to work with other backends](https://github.com/uwescience/myria-web/pull/212) such as Grappa and C.

All this great work is making the system and the research project much powerful and much better, increasing its visibility, benefiting the entire effort, and it fulfills our grant obligations.

However, there is a definite tension here, because running a public service tends to lead to high load on a cluster. At the same time, for our own research, we need to reserve the cluster in order to, e.g., give demos with little resource contention, or perform research experiments with repeatable results.

How should/how can we balance these two concerns?

Until recently, we have relied on a relatively light workload with few real users who were unlikely to interfere with demos or experiments, and we would notify these users when we had a reservation scheduled. But now that we're succeeding -- now that we've advertised to a broader audience and they actually want to use our service -- we need a new strategy.

For now, we've implemented a short-term workaround: [a public Google calendar listing our group's reservations](https://www.google.com/calendar/embed?src=cs.washington.edu_i1gk4il65dj31mcfgid1t9t1o8@group.calendar.google.com&ctz=America/Los_Angeles&mode=week), and [visible warnings on the Myria query editor](https://github.com/uwescience/myria-web/issues/186) when the cluster is reserved. With our friendly users, this is likely good enough. (Our group also has the ability to kill queries if we need to in order to give a demo.)

Long-term, we need to figure out a good balance. On the one hand, the service that we committed to offer has value for the community and generates research ideas, research input, validation, experience, and publicity for our team. On the other hand, serving other groups need not come at the expense of the database group's ability to do research.

One key contributor here will be increased usage of the cloud: for one-time, 24-hour dedicated experiments, it makes more sense to spin up a virtual cloud cluster than it does to stop everything running on our hardware including (but not limited to) the existing Myria service. With the cloud, and unlike our silicon, two different students can work at the same time!

What other advice do you have?