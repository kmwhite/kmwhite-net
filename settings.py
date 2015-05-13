AUTHOR = u'Kristofer M White'
SITENAME = u'kmwhite.net'
SITEURL = u'http://www.kmwhite.net'
TIMEZONE = 'America/Chicago'
THEME = 'kmwhite'

DISQUS_SITENAME = 'kmwhite'

GITHUB_URL = 'http://github.com/kmwhite/'
TWITTER_USERNAME = '_kmwhite'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = 'C'
DEFAULT_PAGINATION = 4

# List found at:
# http://pythonhosted.org/Markdown/extensions/
MD_EXTENSIONS = [
    'markdown.extensions.codehilite',
    'markdown.extensions.fenced_code',
    'markdown.extensions.footnotes',
]

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('Techno-Geeks', 'http://www.techno-geeks.org/'),)

SOCIAL = (('twitter', 'http://twitter.com/_kmwhite'),
          ('github', 'http://github.com/kmwhite'),
          ('bitbucket', 'http://bitbucket.org/kmwhite'))

# global metadata to all the contents
# DEFAULT_METADATA = (('yeah', 'it is'),)

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
