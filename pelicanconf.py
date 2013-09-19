#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jared Kibele'
SITENAME = u'dataFight'
SITEURL = 'http://datafight.com'
SITESUBTITLE = 'struggling with my data, using data against my foes'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('My Bitbucket', 'https://bitbucket.org/jkibele/'),
#          ('My UoA Page', 'http://www.marine.auckland.ac.nz/uoa/jared-kibele'),
#          ('My Other Blog', 'http://www.svarchiteuthis.com/'),
#        )

# Social widget
SOCIAL = (('Bitbucket', 'https://bitbucket.org/jkibele/'),
          ('University of Auckland', 'http://www.marine.auckland.ac.nz/uoa/jared-kibele'),
          ('My Other Blog', 'http://www.svarchiteuthis.com/'),
          ('g+', 'https://plus.google.com/u/0/103120755438399923172'),
        )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-octopress-theme"

PLUGIN_PATH = '/home/jkibele/install/pelican-plugins'
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook']

NOTEBOOK_DIR = '/home/jkibele/Ubuntu One/JobStuff/PhD/iPythonNotebooks'

EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

STATIC_PATHS = [ 'extra/CNAME' ]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    }
#FILES_TO_COPY = ( ('extra/CNAME', 'CNAME'), )