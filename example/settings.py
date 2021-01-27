"""
Django settings for example project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from django.utils.translation import gettext_lazy as _
import os
import re


# Internationalization and localization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    # Customize this
    ('it', _('Italian')),
    ('en', _('English')),
    ('es', _('Spaniel')),
    ('fr', _('French')),
    ('de', _('German')),
    ('ru', _('Russian')),
    ('cn', _('Chinese')),
)

# --- Error Manager
# https://docs.djangoproject.com/en/1.8/howto/error-reporting/#django.views.debug.SafeExceptionReporterFilter

IGNORABLE_404_URLS = [
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
]

# List of Admin users to be emailed by error system
MANAGERS = (
    ('DLRSP', 'dlrsp.dev@gmail.com'),
)
ADMINS = MANAGERS

# Email Settings
EMAIL_HOST = ''  # <--'a real smtp server'
EMAIL_HOST_USER = ''  # <--'your_mailbox_username'
EMAIL_HOST_PASSWORD = ''  # <--'your_mailbox_password'
DEFAULT_FROM_EMAIL = ''  # <--'a real email address'
SERVER_EMAIL = ''  # <--'a real email address'
# --- Error Manager

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Root directory for this django project
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, 'example'))

# Directory where working files, such as media and databases are kept
WORK_DIR = os.path.abspath(os.path.join(BASE_DIR, 'workdir'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e1bt9i8u14_c!s8zi0b@5uqunn137+^vvo7$gj-6#z3&858h!w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Application definition
# https://docs.djangoproject.com/en/1.8/ref/applications/
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'django_errors',
    'example'
]

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_INCLUDE_EXE = 1
# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=django_errors',
]

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    # 'django.middleware.doc.XViewMiddleware',						# <-- Deprecated till 1.8
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.common.BrokenLinkEmailsMiddleware',			# <-- Error Manager 404
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # <-- Common Vulnerability
)
MIDDLEWARE = MIDDLEWARE_CLASSES

ROOT_URLCONF = 'example.urls'

# Template
# https://docs.djangoproject.com/en/1.8/topics/templates/

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
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

# Deploy
# https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
WSGI_APPLICATION = 'example.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(WORK_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.8/ref/settings/#auth-password-validators

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# Staticfiles Config
STATIC_ROOT = os.path.join(WORK_DIR, 'staticroot')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static')
]

# Logging
# https://docs.djangoproject.com/en/1.8/topics/logging/
LOGGING = {
    'version': 1,
    "disable_existing_loggers": False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            # 'class': 'django.utils.log.AdminEmailHandler'			# <-- Error Manager 404
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        "root": {
            "handlers": ["console"],
            'propagate': True,
            "level": "INFO",
        },
        'socialprofile': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
