#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kristofer M White'
SITENAME = 'kmwhtie.net - Random Bathering of a Self-Taught Programmer'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TWITTER_USERNAME = '_kmwhite'
DISQUS_SITENAME = 'kmwhite'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Techno-Geeks', 'http://www.techno-geeks.org/'))

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/_kmwhite'),
          ('github', 'http://github.com/kmwhite'),
          ('bitbucket', 'http://bitbucket.org/kmwhite'))

DEFAULT_PAGINATION = 10

# Document-relative URLs
RELATIVE_URLS = True

# List found at:
# http://pythonhosted.org/Markdown/extensions/
MD_EXTENSIONS = [
    'markdown.extensions.abbr',
    'markdown.extensions.admonition',
    'markdown.extensions.codehilite',
    'markdown.extensions.def_list',
    'markdown.extensions.fenced_code',
    'markdown.extensions.footnotes',
    'markdown.extensions.toc',
]

# Static paths will be copied under the same name
STATIC_PATHS = [
    'images',
    'extra/.htaccess',
    'extra/composer.json',
    'extra/favicon.ico',
    'extra/robots.txt',
]

# A lit of extra attrs to respect when traversing STATIC_PATHS,
# including altering destination paths
EXTRA_PATH_METADATA = {
    'extra/.htaccess':     {'path': '.htaccess'},
    'extra/composer.json': {'path': 'composer.json'},
    'extra/favicon.ico':   {'path': 'favicon.ico'},
    'extra/robots.txt':    {'path': 'robots.txt'},
}
