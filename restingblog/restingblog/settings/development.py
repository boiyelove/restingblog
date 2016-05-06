"""
Django settings for restingblog project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import os
from .base import *

#development settings live here

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#As defined below, host, name, port, user, password are optional
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # settings for the first database oracle
    'firstdsb': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'my_database',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
    
    },
    # settings for the second database mysql
    'secondb': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_database',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
        
    },
    # settings for the third database oracle 
    'thirddb': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'my_database',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
    
    },
    # settings for the fourth database: mongodb
    'forthdb': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'my_database',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
    },
    # settings for the fourth database: mongodb
    'replica': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'HOST': 'dbreplica',
        'TEST': {
            'MIRROR': 'default',
        },
        # ... plus some other settings
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


