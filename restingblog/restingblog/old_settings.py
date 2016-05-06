"""
Django settings for restingblog project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sou0$-u#=r^&315#-^hr!+^-107jss#3nb$3#4)ep+iea6u9(n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts.apps.PostsConfig',
    'rest_framework',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restingblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'restingblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#As defined below, host, name, port, user, password are optional
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # settings for the first database oracle
    'firstdsb': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'my_database',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
    
    }
    # settings for the second database mysql
    'secondb': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_database',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
        
    }
    # settings for the third database oracle 
    'thirddb': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'my_database',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
    
    }
    # settings for the fourth database: mongodb
    'forthdb': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'my_database',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
    }
    # settings for the fourth database: mongodb
    'replica': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'HOST': 'dbreplica',
        'TEST': {
            'MIRROR': 'default',
        },
        # ... plus some other settings
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


'''
REST FRAMEWORK
We'd also like to set a few global settings. 
We'd like to turn on pagination, 
and we want our API to only be accessible to admin users. 
The settings module will be in settings.py
'''

REST_FRAMEWORK = {
    # Use Django's standard 'django.contrib.auth' permissions,
    # or allow read-only access for unauthenticated users.
    
    'DEFAULT_PPERMISSION_CLASSES': ('rest_framework.permisions.DjangoModelPermissionsOrAnonReadOnly',),
    'PAGE_SIZE' : 10

# Adding pagination
# The list views for users and code snippets could end up returning quite a lot of instances,
# so really we'd like to make sure we paginate the results, and allow the API client to step
# through each of the individual pages.
# Note that settings in REST framework are all namespaced into 
# a single dictionary setting, named 'REST_FRAMEWORK', 
# which helps keep them well separated from your other project settings.
}
