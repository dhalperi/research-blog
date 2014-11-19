Title: Mozilla, eScience
Date: 2014-11-14
Category: daily
Tags: camille, mozilla, escience

Last month, I grabbed a beer with [Kay Thaney](http://kaythaney.com/) and chatted about various M/S and Data Science and eScience and other activities; it was a great chat. One consequence is that Kay invited [Jake VanderPlas](http://www.astro.washington.edu/users/vanderplas/) and I to present about the [Data Science Incubator](http://data.uw.edu/incubator) on the [Mozilla Science Lab Call](https://etherpad.mozilla.org/sciencelab-calls-nov13-2014) yesterday. We spent 5 or 10 minutes explaining what the what the eScience Institute is, what the Data Science Incubator is, giving some example participants, and taking questions. You can see the call notes at the linked [Etherpad](https://etherpad.mozilla.org/sciencelab-calls-nov13-2014).

We began interviews for a [web content strategist](https://uwhires.admin.washington.edu/eng/candidates/default.cfm?szCategory=jobprofile&szOrderID=112161) today. More on that when I'm allowed to talk about it.

Finally, I met with [Camille](http://r.halper.in/people/cobbc12) to discuss her work on automatically generating visualizations. This work has been greatly advanced by conversations I had with viz-whiz [Aritra Dasgupta](http://vgc.poly.edu/~adasgupta/) at NYU last month, and we now have a concrete idea for how to frame the problem. Here's the question:

* Overall problem: a user loads a dataset and then executes a series of automated, semi-automated, or manual steps to specify a visualization.
* Existing, commonly-used tools for this task include Tableau, IPython Notebook, etc., each of which has its own strengths and weaknesses.

**Question**: does knowing the query/queries that generated the dataset let you automate more? In particular, given the dataset and queries alone, can we suggest the visualization the user wants to draw? What if we add workload information?

We're confident the answer to these is "yes". More to come!