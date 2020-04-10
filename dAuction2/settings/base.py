"""
Django settings for dAuction2 project.
"""
import os
from django.conf.urls import url
# BASEDIR is the folder where manage.py is
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'..'))
UNIQUEIZER = 1000000
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.split(PROJECT_DIR)[0]
VAGRANT_INSTANCE_FOLDER = 'C:/dAuction/dAuction2'
# PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k#!q9vjjynr)aaqxam50f*pgzwt9cj3j#rkd^@^%r(air1w7f%'

PASSWORD_HASHERS = ('passwords_plaintext.PlainTextPassword',)
CONN_MAX_AGE=500
# LOGOUT_REDIRECT_URL = 'master/login_user'

# Read it fro os.ENV
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG = True
DEBUG_PERFORMANCE = False

OUR_LOGGING = True
# This is secure, overide your defaults in local.py
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'whitenoise',
    'django.contrib.staticfiles',
    'dAuction2',
    'experiment',
    'master',
    'instructions',
    'distribution',
    'testing',
    'master_data',
    'master_earn',
    'master_sanl',
    'forward_and_spot',
    'questionnaire',
    'payout',
    'api',
    'pyom',
    'rest_framework',
    'anl'
]



#an experiment has maximally these stages
SESSION_STAGES_FULL = ['dAuction2','instructions','distribution','testing','forward_and_spot','questionnaire','payout']

# # the particular (still "hardcoded") experiment has these stages
# SESSION_STAGES = ['instructions','distribution','testing','forward_and_spot','questionnaire','payout']
SESSION_STAGES_RELEVANT = set(INSTALLED_APPS) & set(SESSION_STAGES_FULL)

if DEBUG and DEBUG_PERFORMANCE:
    INSTALLED_APPS += (
        'debug_toolbar',
        'debug_panel',
    )
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": True,
        'RESULTS_CACHE_SIZE': 60,
    }


INTERNAL_IPS = ('0.0.0.0','127.0.0.1')

# def show_toolbar(request):
#     return True


MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',

    # place all other middlewares here
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'yet_another_django_profiler.middleware.ProfilerMiddleware',
    # from Jan: 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

# # Key in `CACHES` dict
# CACHE_MIDDLEWARE_ALIAS = 'default'
# # Additional prefix for cache keys
# CACHE_MIDDLEWARE_KEY_PREFIX = ''
# # Cache key TTL in seconds
# CACHE_MIDDLEWARE_SECONDS = 600


if DEBUG and DEBUG_PERFORMANCE:
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'debug_panel.middleware.DebugPanelMiddleware',
                           )
    PROFILING_SQL_QUERIES =True

ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'dAuction2.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
# USE_I18N = True
USE_I18N = False # translation!
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# STATIC_ROOT = 'staticfiles'
STATIC_URL = '/staticfiles/'

# STATIC_URL = '/assets/'
# STATIC_ROOT = str(ROOT_DIR.path('assets'))

# STATICFILES_DIRS = (
#     str(ROOT_DIR.path('static')),
# )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Sicne we use Vagrant for developemnt, this is save. For production server
# configure another credentials
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dauction2',
        'USER': 'dauction',
        'PASSWORD': 'dauction',
        'HOST': '127.0.0.1',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

SITE_ROOT = os.path.join(BASE_DIR, 'logs')
OUR_LOGGING_FS = True
# OUR_LOGGING_FS = False

if OUR_LOGGING_FS:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                # 'format' : "[%(asctime)s] %(levelname)s [%(name)s: %(funcName)s : %(lineno)s] %(message)s",
                # 'format': "[%(asctime)s] %(levelname)s [%(filename)s - %(funcName)s: %(lineno)s] %(message)s",
                'format': "[%(asctime)s] %(levelname)s %(pathname)s - %(funcName)s: %(lineno)s] %(message)s",
                # 'datefmt' : "%d/%b/%Y %H:%M:%S"
                # 'datefmt': "%d- %H:%M:%S"
                # 'datefmt': "%d/%b- %H:%M:%S:%f"
            },
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',
            },

            'logfile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': SITE_ROOT + "/dAuction_logfile",
                # 'formatter':'%(asctime)s %(message)s', # include timestamp
                # 'maxBytes': 50000,
                'backupCount': 2,
                'formatter': 'standard',
            },

            'logfile_F&S': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': SITE_ROOT + "/dAuction_logfile",
                # 'formatter':'%(asctime)s %(message)s', # include timestamp
                # 'maxBytes': 50000,
                'backupCount': 2,
                'formatter': 'standard',
            },

            'logfile_SVK': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': SITE_ROOT + "/dAuction_logfile_SVK_DEBUG",
                # 'formatter':'%(asctime)s %(message)s', # include timestamp
                # 'maxBytes': 50000,
                'backupCount': 2,
                'formatter': 'standard',
            },

            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },

        },
        'loggers': {
            'debug_logger': {
                'handlers': ['logfile_SVK'],
                'level': 'DEBUG'
            },

            'django': {
                'handlers': ['console'],
                'propagate': True,
                'level': 'WARN',
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'api': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'instructions': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'forward_and_spot': {
                'handlers': ['console', 'logfile_F&S'],
                'level': 'DEBUG',
            },
            'master': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'master_earn': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'master_data': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'master_sanl': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'payout': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'questionnaire': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'testing': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'distribution': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'dAuction2': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
        }
    }
elif OUR_LOGGING:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                # 'format' : "[%(asctime)s] %(levelname)s [%(name)s: %(funcName)s : %(lineno)s] %(message)s",
                'format': "BB[%(asctime)s] %(levelname)s %(module)s-[%(filename)s - %(funcName)s: %(lineno)s] %(message)s",
                # 'datefmt' : "%d/%b/%Y %H:%M:%S"
                # 'datefmt': "%d- %H:%M:%S"
                'datefmt': "%d/%b- %H:%M:%S:%f"
            },
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',
            },

            'logfile': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': SITE_ROOT + "/dAuction_logfile",
                # 'formatter':'%(asctime)s %(message)s', # include timestamp
                #'maxBytes': 50000,
                'backupCount': 2,
                'formatter': 'standard',
            },

            'logfile_F&S': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': SITE_ROOT + "/dAuction_logfile",
                # 'formatter':'%(asctime)s %(message)s', # include timestamp
                # 'maxBytes': 50000,
                'backupCount': 2,
                'formatter': 'standard',
            },

            'logfile_SVK': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': SITE_ROOT + "/dAuction_logfile_SVK_DEBUG",
                # 'formatter':'%(asctime)s %(message)s', # include timestamp
                # 'maxBytes': 50000,
                'backupCount': 2,
                'formatter': 'standard',
            },

            'console':{
                'level':'INFO',
                'class':'logging.StreamHandler',
                'formatter': 'standard'
            },

            'error_logfile': {
                'level': 'ERROR',
                # 'filters': ['require_debug_false'],  # run logger in production
                'class': 'logging.FileHandler',
                'filename': os.path.join(SITE_ROOT, 'error.log'),
                'formatter': 'standard'
            },

        },
        'loggers': {
            'debug_logger': {
                'handlers': ['logfile_SVK'],
                'level': 'DEBUG'
            },

            'django': {
                'handlers':['console'],
                'propagate': True,
                'level':'WARN',
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'api': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'forward_and_spot': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'master': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'instructions': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
            'master_earn': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
             'distribution': {
                'handlers': ['console', 'logfile'],
                'level': 'DEBUG',
            },
        }
    }
else:
    LOGGING_CONFIG = None


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#         'TIMEOUT': 60000
#     }
# }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': None,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }

    }
}

# CACHES = {
#     'default': {
#         # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

AUTH_USER_MODEL = 'dAuction2.User'





