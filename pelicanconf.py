#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Daniel Halperin'
SITENAME = u"Dan's research blog"
SITEURL = 'http://blog.halper.in'

PATH = 'content'
DISPLAY_CATEGORIES_ON_MENU = True

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
TAG_FEED_ATOM = "feeds/%s.atom.xml"

# DISQUS comments
DISQUS_SITENAME = "blog-halper-in"

# GA
GOOGLE_ANALYTICS = "UA-54311387-1"

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

THEME = "notmyidea"

# DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Use pretty typesetting
TYPOGRIFY = True

STATIC_PATHS = ['CNAME', 'images']

# Where to look for plugins
PLUGIN_PATHS = ['pelican-plugins']
# Which plugins to enable
PLUGINS = ['better_figures_and_images']
# Responsive images
RESPONSIVE_IMAGES = True
