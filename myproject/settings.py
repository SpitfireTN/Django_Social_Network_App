"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from typing import Union

from django.contrib.messages import constants as messages
from dotenv import load_dotenv

# Loading ENV
env_path: Path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

SITE_NAME = "CSCTN.net"
SITE_DOMAIN = "www.csctn.net"
PROTOCOL = "http"
# PROTOCOL = "https"

INTERNAL_IPS = [
    "192.168.2.115",
    "127.0.0.1",
]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR: Path = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY: Union[str, None] = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG: Union[str, None] = os.getenv("DEBUG")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/web/dsn/logs/debug.log",
        },
        "daphne_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/web/dsn/logs/daphne_debug.log",
        },
    },
    "loggers": {
        "root": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
        "daphne": {
            "handlers": [
                "daphne_file",
            ],
            "level": "DEBUG",
        },
    },
}

ALLOWED_HOSTS: list[str] = ["*"]


# Application definition

INSTALLED_APPS: list[str] = [
    "crispy_forms",
    # "daphne",
    "django_cleanup",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "bootstrap_datepicker_plus",
    "django_tables2",
    "ckeditor",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.github",
    "debug_toolbar",
    "blog.apps.BlogConfig",
    "users.apps.UsersConfig",
    "notification",
    "chat",
    "channels",
    "friend",
    "videocall",
    "EventManager",
    "events",
]

MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

# DEBUG_TOOLBAR_CONFIG = {

# }

ROOT_URLCONF: str = "myproject.urls"

TEMPLATES: list[dict[str, Union[bool, str, dict[str, list[str]]]]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "users/templates"),
            os.path.join(BASE_DIR, "events/templates"),
        ],
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

AUTHENTICATION_BACKENDS: list[str] = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

WSGI_APPLICATION: str = "myproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES: dict[str, dict[str, str]] = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'socialNet',
#         'USER': 'postgres',
#         'PASSWORD': os.getenv("PGDB_PWD"),
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE: str = "en-us"

TIME_ZONE: str = "America/New_York"

USE_I18N: bool = True

USE_L10N: bool = True

USE_TZ: bool = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATICFILES_FINDERS: tuple[str] = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

STATICFILES_DIRS: list[str] = [
    "/web/dsn/blog/static",
]

STATIC_URL: str = "static/"

EMAIL_TEMPLATE_ROOT: str = os.path.join(BASE_DIR, "email_templates")

MEDIA_ROOT: str = os.path.join(BASE_DIR, "media")
MEDIA_URL: str = "/media/"

CRISPY_TEMPLATE_PACK: str = "bootstrap4"

LOGIN_REDIRECT_URL: str = "profile"
LOGIN_URL: str = "account_login"

CKEDITOR_CONFIGS: dict[str, dict[str, str]] = {
    "default": {
        "width": "auto",
    },
}

EMAIL_BACKEND: str = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST: str = "smtp.gmail.com"
EMAIL_PORT: str = os.getenv("EMAIL_TLS_PORT")
EMAIL_USE_TLS: str = True
DEFAULT_FROM_EMAIL: str = "bubbaandy89@gmail.com"
EMAIL_HOST_USER: str = os.getenv("EMAIL_USER")  # environment variable containing username
EMAIL_HOST_PASSWORD: str = os.getenv("EMAIL_PASS")  # environment variable containing password

GOOGLE_RECAPTCHA_SECRET_KEY: str = os.getenv("GOOGLE_RECAPTCHA_SECRET_KEY")

MESSAGE_TAGS: dict[int, str] = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

ASGI_APPLICATION: str = "myproject.routing.application"

CHANNEL_LAYERS: dict[str, dict[str, str]] = {
    "default": {"BACKEND": "channels_redis.core.RedisChannelLayer"},
    "CONFIG": {
        "hosts": [("127.0.0.1", 6379)],
    },
}

SITE_ID: int = 2  # considering 2nd site in 'Sites' to be 127.0.0.1 (for dev)

SOCIALACCOUNT_PROVIDERS: dict[str, dict[str, list[str]]] = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
    "github": {
        "SCOPE": [
            "user",
            "repo",
            "read:org",
        ],
    },
}
