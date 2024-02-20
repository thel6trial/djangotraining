"""
Django settings for djangotraining project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIgôR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/images/'
MEDIA_ROOT = "/var/www/static/images/"
UPLOAD_ROOT = "%s/_upload" % MEDIA_ROOT

LOGIN_REDIRECT_URL = '/blog/main'

#AUTH_USER_MODEL = 'blog.User'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2t))0ounvj7a^&1ienfd)au&*5ia@)luj^!%+kph@lf0vr$#g@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost', '0.0.0.0']

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1',
    'http://localhost:8000',
]

AUTH_USER_MODEL = 'blog.User'


# Application definition

INSTALLED_APPS = [
    "daphne",
    "django.contrib.sites",
    "blog.apps.BlogConfig",
    "blog.templatetags",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ckeditor",
    "channels",
    "celery",
    "djangotraining",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "blog.middleware.CustomErrorMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "djangotraining.urls"

CSRF_COOKIE_SECURE = False

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "blog/templates/",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
            ],
        },
    },
]

#WSGI_APPLICATION = "djangotraining.wsgi.application"

ASGI_APPLICATION = 'djangotraining.asgi.application'

ASGI_APPLICATION_TIMEOUT = 60

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "blogdb",
        "USER": "root",
        "PASSWORD": "password",
        "HOST": "db",
        "PORT": "3306",
        'OPTIONS': {
            'read_default_file': '/opt/lampp/etc/my.cnf',
        }
    }
}

CELERY_APP = 'djangotraining.celery:app'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_BROKER_URL = 'redis://djangotraining-redis-1:6379/0'
CELERY_RESULT_BACKEND = 'redis://djangotraining-redis-1:6379/0'
CELERY_IMPORTS = ("blog.tasks",)

CELERY_BEAT_SCHEDULE = {
    'send_hourly_notification_email': {
        'task': 'send_hourly_notification_email',
        'schedule': 3600.0, 
    },
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = "static/"

CKEDITOR_BASEPATH = "blog/static/assets/ckeditor/ckeditor/"

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js' 

CKEDITOR_CONFIGS = {
    'default':
        {
            'toolbar': 'full',
            'width': 'auto',
            'extraPlugins': ','.join([
                'codesnippet',
            ]),
        },
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEFAULT_FROM_EMAIL = 'nhloc610@gmail.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'nhloc610@gmail.com'
EMAIL_HOST_PASSWORD = 'knhx ntje lcbb drpv'
EMAIL_USE_TLS = True


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "custom": {
            "format": "%(asctime)s %(levelname)s %(message)s --------------------------------",
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "djangotraining/debug.log",
            "formatter": "custom",
        },
    },
    "root": {
        "handlers": ["file"],
        "level": "WARNING",
    },
    # "loggers": {
    #     "django": {
    #         "handlers": ["file"],
    #         "level": "DEBUG",
    #         "propagate": True,
    #     },
    # },
}

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '884960344275-9l4givqj3p4m12k36ppcndqslffgn99f.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SITE_ID = 4

GOOGLE_CLIENT_ID = '884960344275-l4toda8c3u1u8em9tg88jfgtsb5qucg9.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_REDIRECT_URI = 'http://localhost/blog/google/callback'

FACEBOOK_APP_ID = '629942819263173'
FACEBOOK_APP_SECRET = 'ec14664516d110bd951229548e16600f'
FACEBOOK_REDIRECT_URI = 'http://localhost/blog/facebook/callback'

TWITTER_CONSUMER_KEY='1758396050178760705-fmIQclDR814GUNqoUNPu7wofXxSvsv'
TWITTER_CONSUMER_SECRET='rNVZK0XU1Vu6TBaeGNjKml81pRNmrBKPchkBR8WVacfbm'
TWITTER_REDIRECT_URI = 'http://localhost/blog/twitter/callback'

LINE_CHANNEL_ID = '2003655941'
LINE_CHANNEL_SECRET = 'd326124c751e6f252b120a08c6bb8c54'
LINE_REDIRECT_URI = 'http://localhost/blog/line/callback'

LINE_MESSAGE_ID = '2003657318'
LINE_MESSAGE_SECRET = '54b937e3784311e7eae06f0850b69023'
LINE_MESSAGE_ACCESS = 'aYJB9xetorvgBBbyUrBQLhrpk7RFX7fHNAEJ7wYoL6yUz7FxlOfby44YGfgiFBhXFLMcRg9JKmrQ/AQGn33jXnvb1mEfodueEgllAuxx2EiFvkE9H4nK6vXKYKtfsvE4a4Hu1PkuPqtirzi9bZjK6wdB04t89/1O/w1cDnyilFU='
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'APP': {
#             'client_id': '884960344275-7g2nc5nmogcofm6aqg9b93vld8q9ngtm.apps.googleusercontent.com',
#             'secret': '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',
#             'key': ''
#         },
#         "INIT_PARAMS": {"redirect_uri": "http://localhost/blog/google/callback"},
#         'SCOPE': ['profile', 'email'],  
#         'AUTH_PARAMS': {'access_type': 'online'},
#     }
# }

# SCIALACCOUNT_PROVIDERS = {
#     'facebook': {
#         'APP': {
#             'client_id': '766276934958473',
#             'secret': 'aa118ce99baab0fe8df612afc75ed1c2',
#             'key': ''
#         },
#         'SCOPE': ['profile', 'email'],  
#         'AUTH_PARAMS': {'access_type': 'online'},
#         'INIT_PARAMS': {'redirect_uri': 'http://localhost/blog/facebook/callback/'},
#     }
# }


ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = False 
ACCOUNT_EMAIL_REQUIRED = True