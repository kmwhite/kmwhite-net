AUTHOR = u'Kristofer M White'
SITENAME = u'kmwhite.net'
SITEURL = u'http://www.kmwhite.net'
TIMEZONE = "America/Chicago"
THEME = 'kmwhite'

DISQUS_SITENAME = 'kmwhite'

GITHUB_URL = 'http://github.com/kmwhite/'
TWITTER_USERNAME = '_kmwhite'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('Techno-Geeks', "http://www.techno-geeks.org/"),)

SOCIAL = (('twitter', 'http://twitter.com/_kmwhite'),
          ('github', 'http://github.com/kmwhite'),
          ('bitbucket', 'http://bitbucket.org/kmwhite'))

# global metadata to all the contents
# DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["images", ]

# A list of files to copy from the source to the destination
STATIC_PATHS = [
    'extra/robots.txt',
    'extra/.htaccess',
    'extra/index.php',
    'extra/favicon.ico',
]

EXTRA_PATH_METADATA = {
    'extra/composer.json': {'path': 'composer.json'},
    'extra/robots.txt':    {'path': 'robots.txt'},
    'extra/.htaccess':     {'path': '.htaccess'},     # Disable PHP
    'extra/index.php':     {'path': 'index.php'},     # Trick Heroku
    'extra/favicon.ico':   {'path': 'favicon.ico'},
}
