#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'john wamburu'
SITENAME = u'John Mbari Wamburu'
SITEURL = 'http://www.johnwamburu.me'

PATH = 'content'

TIMEZONE = 'Africa/Nairobi'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('Github', 'http://github.com/jwamburu'),
    ('Twitter', 'http://twitter.com/johnwamburu'),
    ('LinkedIn', 'https://ke.linkedin.com/in/johnwamburu'),
)

DEFAULT_PAGINATION = 2

STATIC_PATHS = ['images', 'pdfs']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "johnwamburu"
GOOGLE_ANALYTICS = "UA-67521796-1"

THEME = "pelican-svbhack"

TAGLINE = ""

USER_LOGO_URL = SITEURL + '/images/john-mbari-wamburu.JPG'

LOAD_CONTENT_CACHE = False
