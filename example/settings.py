"""
Django settings for example project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import re

import django_heroku
from django.utils.translation import gettext_lazy as _

SITE_ID = 1

# Internationalization and localization
LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ("de", _("German")),
    ("en", _("English")),
    ("es", _("Spaniel")),
    ("fi", _("Suomi")),
    ("fr", _("French")),
    ("it", _("Italian")),
    ("ru", _("Russian")),
    ("no", _("Norsk")),
    ("nl", _("Dutch")),
    ("ja", _("日本語")),
    ("zh-cn", _("简体中文")),
    ("zh-tw", _("繁體中文")),
)

IGNORABLE_404_URLS = [
    re.compile(r"^/apple-touch-icon.*\.png$"),
    re.compile(r"^/favicon\.ico$"),
    re.compile(r"^/robots\.txt$"),
]

# List of Admin users to be emailed by error system
MANAGERS = (("DLRSP", "dlrsp.dev@gmail.com"),)
ADMINS = MANAGERS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Root directory for this django project
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, "example"))

# Directory where working files, such as media and databases are kept
WORK_DIR = os.path.abspath(os.path.join(BASE_DIR, "workdir"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "e1bt9i8u14_c!s8zi0b@5uqunn137+^vvo7$gj-6#z3&858h!w"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["0.0.0.0", "localhost", "127.0.0.1", "django-errors.herokuapp.com"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "robots",
    "easy_thumbnails",
    "filer",
    "mptt",
    "django_errors",
    "example",
]

EMAIL_HOST = ""
EMAIL_PORT = "25"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ""

MIDDLEWARE = (
    # "django.middleware.common.BrokenLinkEmailsMiddleware",  # <-- Error Manager 404
    "django_errors.middleware.handler.HttpResponseNotAllowedMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    "django.middleware.http.ConditionalGetMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
)

ROOT_URLCONF = "example.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Deploy
WSGI_APPLICATION = "example.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(WORK_DIR, "db.sqlite3"),
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Absolute path to the directory that holds media.
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(WORK_DIR, "mediaroot")

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(WORK_DIR, "staticroot")

# THUMBNAIL
THUMBNAIL_PREFIX = "thumbs_"
THUMBNAIL_NAMER = "easy_thumbnails.namers.source_hashed"
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    # 'easy_thumbnails.processors.scale_and_crop',
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        + "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation." + "MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation." + "CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation." + "NumericPasswordValidator",
    },
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(WORK_DIR, "staticroot")
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d "
            + "%(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "mail_admins": {
            "level": "ERROR",
            # 'class': 'django.utils.log.AdminEmailHandler'			# <-- Error Manager 404
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "root": {
            "handlers": ["console"],
            "propagate": True,
            "level": "INFO",
        },
        "django": {
            "handlers": ["console"],
            "propagate": True,
            "level": "INFO",
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}

if DEBUG:
    # Use nose to run all tests
    INSTALLED_APPS.append("django_nose")
    TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
    NOSE_INCLUDE_EXE = 1
    NOSE_ARGS = [
        "--with-coverage",
        "--cover-package=django_errors",
    ]

if os.environ["DYNO"]:
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    MIDDLEWARE = MIDDLEWARE + ("whitenoise.middleware.WhiteNoiseMiddleware",)
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    django_heroku.settings(locals())
