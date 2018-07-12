#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kristofer M White'
SITENAME = 'kmwhite.net'
WELCOME_MESSAGE = 'random blathering from a software janitor'
SITEURL = ''
LOGOPATH = '/theme/images/avatar.jpg'
THEME = 'semantic-ui'
THEME_VARIANT = 'darkly'

PATH = 'content'

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

INCLUDE_SOCIAL_SHARE_LINKS = False
INCLUDE_FOOTER = True
INCLUDE_FOOTER_VERTICAL = False
INCLUDE_FOOTER_HORIZONTAL = True

TWITTER_USERNAME = '_kmwhite'
# DISQUS_SITENAME = 'kmwhite'
GITHUB_USERNAME = 'kmwhite'

# Blogroll
MENU_LINKS = (
    ('twitter', 'http://twitter.com/_kmwhite'),
    ('github', 'http://github.com/kmwhite'),
    ('bitbucket', 'http://bitbucket.org/kmwhite')
)
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('Techno-Geeks', 'http://www.techno-geeks.org/')
)


DEFAULT_PAGINATION = 10

# Document-relative URLs
RELATIVE_URLS = True

# Static paths will be copied under the same name
STATIC_PATHS = [
    'images',
    'extra/.htaccess',
    'extra/composer.json',
    'extra/favicon.ico',
    'extra/robots.txt',
]

# A list of extra attrs to respect when traversing
# STATIC_PATHS, including altering destination paths
EXTRA_PATH_METADATA = {
    'extra/.htaccess':     {'path': '.htaccess'},
    'extra/composer.json': {'path': 'composer.json'},
    'extra/favicon.ico':   {'path': 'favicon.ico'},
    'extra/robots.txt':    {'path': 'robots.txt'},
}
