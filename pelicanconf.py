#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Daniel Halperin'
SITENAME = u"Dan's research blog"
SITEURL = 'http://blog.halper.in'

PATH = 'content'
DISPLAY_CATEGORIES_ON_MENU = False

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# DISQUS comments
DISQUS_SITENAME = "blog-halper-in"

# Blogroll
LINKS = (('Pythonic Perambulations', 'http://jakevdp.github.io/'),)

# Menu items
MENUITEMS = (('Homepage', 'http://r.halper.in/work'), )

# Social widget
TWITTER_USERNAME = 'dhalperi'
SOCIAL = (('GitHub', 'https://github.com/dhalperi'),
          ('ImpactStory', 'https://impactstory.org/DanielHalperin'),
          ('Scholar', 'https://scholar.google.com/citations?user=C6k0OjMAAAAJ'),
          ('Twitter', 'https://twitter.com/dhalperi'),
          ('Google+', 'https://plus.google.com/+DanielHalperin'))

# DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Use pretty typesetting
TYPOGRIFY = True

STATIC_PATHS = ['CNAME']
