# -*- coding: utf-8 -*-
from .base import TEMPLATES, INSTALLED_APPS, LOGGING, MIDDLEWARE_CLASSES

DEBUG=True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions'
]


def custom_show_toolbar(self):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
}

LOGGING['loggers']['forward_and_spot']['level'] = 'DEBUG'

