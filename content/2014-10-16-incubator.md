Title: SSL certificates suck; Incubator 3.2 → NYU
Date: 2014-10-16
Category: daily
Tags: sophie, incubator

Today was "I-hate-certificates" day. Four different people had ugly issues with SSL:

* [Sophie](http://r.halper.in/coauth/sclayton) has finished cleaning the underway data in SQLShare and is ready to load it into Myria. However, she had problems using Myria's Python client because her Mac did not trust Myria's SSL certificate. (UW's choice of Certificate Authority (CA), InCommon, has apparently not been blessed by Mac OS X.)
* Brendan Lee has been working with the [UW Database Group](http://db.cs.washington.edu/) on [MyMergerTree](http://dl.acm.org/citation.cfm?id=2627774). MyMergerTree is powered by Myria, so after I enabled SSL yesterday, I asked him to fix the web service to use HTTPS instead of HTTP links. Well, great, InCommon has not been blessed by Ubuntu either.
* Two different people came to Incubator office hours to learn about `git`. They brought older laptops with, you guessed it, older versions of Mac OS X installed. And, surprise surprise, [GitHub's current SSL certificate](https://help.github.com/articles/error-ssl-certificate-problem-verify-that-the-ca-cert-is-ok/) is not blessed by those old versions of Mac OS X, and the only way to fix it is to _upgrade the OS_. You know, because that's a _totally reasonable_ option.

Such a waste of time. Why do we make users jump through these hoops? We worked around these issues in a variety of ways, all of which involved disabling certificate verification. Ugh, that's a fail. (In one case we were able to switch from HTTPS to SSH for GitHub -- that, at least, made me moderately less sad at heart.)

I left at lunch for the airport. I'll be at NYU in Brooklyn for the next week giving talks, making connections, and generally getting to know better our Moore-Sloan DSE collaborators across the country. I spent the entire flight working on slides for the various talks.