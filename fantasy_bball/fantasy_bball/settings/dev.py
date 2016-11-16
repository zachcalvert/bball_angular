# export DJANGO_SETTINGS_MODULE=fantasy_bball.settings.dev
from base import *

CURRENT_ENV = 'dev'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'basketball',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3307',
    }
}