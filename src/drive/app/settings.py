import os
from distutils.util import strtobool
from pathlib import Path

from celery.schedules import crontab
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_DIR = BASE_DIR.parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = bool(strtobool(os.getenv("DEBUG")))

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split()

CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS").split()

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

LOCALE_PATHS = (os.path.join(BASE_DIR, "bot/communication/babel/locale/"),)  # noqa

GRPC_SERVICE_PORT = int(os.getenv("GRPC_SERVICE_PORT", 5050))

GRPC_CONCURRENCY = int(os.getenv("GRPC_CONCURRENCY", 10))

INSTALLED_APPS = [
    "jazzmin.apps.JazzminConfig",
    "jsoneditor",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drive.bot.apps.BotConfig",
    "drive.exam.apps.ExamConfig",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "drf_spectacular",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "drive.app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # noqa
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

WSGI_APPLICATION = "drive.app.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")  # noqa
STATICFILES_DIRS = (os.path.join(BASE_DIR, "custom_static"),)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")
MEDIA_ROOT = "drive/media/"


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_SECRET_KEY = os.getenv("TELEGRAM_SECRET_KEY")
BOT_USERNAME = os.getenv("BOT_USERNAME")
PROJECT_URL = os.getenv("PROJECT_URL")
GRPC_API_ADDRESS = os.getenv("GRPC_API_ADDRESS")
PROBLEMS_CHAT_ID = int(os.getenv("PROBLEMS_CHAT_ID"))

# Celery settings

CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TRACK_STARTED = True
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
CELERY_BEAT_SCHEDULE = {
    "search_new_tickets": {
        "task": "drive.exam.tasks.search_new_tickets",
        # "schedule": crontab(minute="0", hour="*/1")
        "schedule": crontab(minute="*/1"),
    }
}


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "drive.api.authentication.CustomTokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "drive.api.permission.ReadOnlyTokenPermission",
    ],
    "DEFAULT_PAGINATION_CLASS": "drive.api.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


SPECTACULAR_SETTINGS = {
    "TITLE": "Drive Tickets Bot API",
    "VERSION": "v1.0.0",
    "DESCRIPTION": "@driveticketsbot",
    "CONTACT": {
        "name": "tg: @anokhinpavel",
        "url": "https://t.me/anokhinpavel",
    },
    "LICENSE": {
        "name": "MIT",
    },
    "SERVE_INCLUDE_SCHEMA": False,
    "SERVERS": [
        {
            "url": PROJECT_URL,
            "description": "Production server",
        }
    ],
}
