# -*- coding: utf-8 -*-
import os
import environ

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_DIR = os.path.join(PROJECT_DIR, 'apps')

# Load operating system environment variables and then prepare to use them
env = environ.Env()

# .env file, should load only in development environment
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=False)

if READ_DOT_ENV_FILE:
    # Operating System Environment variables have precedence over variables defined in the .env file,
    # that is to say variables from the .env files will only be used if not defined
    # as environment variables.
    env_file = os.path.join(PROJECT_DIR, '.env')
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')


SECRET_KEY = env('DJANGO_SECRET_KEY', default='VerySecretKey')

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]
THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]
LOCAL_APPS = [
    'apps.api',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', False)


# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, 'fixtures'),
)


# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')


# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
ADMINS = [
    ("""{{ cookiecutter.author_name }}""", '{{cookiecutter.email}}'),
]
MANAGERS = ADMINS


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres://postgres:postgres@db/postgres'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = False


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
TIME_ZONE = '{{ cookiecutter.timezone }}'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default='*,')
USE_ETAGS = env.bool('DJANGO_USE_ETAGS', True)


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(APPS_DIR, 'templates'),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
if not DEBUG:
    TEMPLATES[0]['OPTIONS']['loaders'] = [
        ('django.template.loaders.cached.Loader', [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]),
    ]


# SECURE DJANGO CONFIGURATION
# ------------------------------------------------------------------------------
SECURE_HSTS_SECONDS = env("SECURE_HSTS_SECONDS", default=0)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool("SECURE_CONTENT_TYPE_NOSNIFF", False)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("SECURE_HSTS_INCLUDE_SUBDOMAINS", False)
SECURE_BROWSER_XSS_FILTER = env.bool("SECURE_BROWSER_XSS_FILTER", False)
SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE", False)
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", False)
CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE", False)
CSRF_COOKIE_HTTPONLY = env.bool("CSRF_COOKIE_HTTPONLY", False)
X_FRAME_OPTIONS = env("X_FRAME_OPTIONS", default="SAMEORIGIN")


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static_root')
STATIC_HOST = env('DJANGO_STATIC_HOST', default='')
STATIC_URL = STATIC_HOST + '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(APPS_DIR, 'static'),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'


# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'


# PASSWORD VALIDATION
# ------------------------------------------------------------------------------
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

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

{% if cookiecutter.use_celery == 'y' %}
########## CELERY
INSTALLED_APPS += ['project.taskapp.celery.CeleryConfig']
BROKER_URL = env('CELERY_BROKER_URL', default='django://')
if BROKER_URL == 'django://':
    CELERY_RESULT_BACKEND = 'redis://'
else:
    CELERY_RESULT_BACKEND = BROKER_URL
########## END CELERY
{% endif %}

# CACHE CONFIGURATION
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCach',
        'KEY_PREFIX': '{{ cookiecutter.project_slug }}',
        'LOCATION': env('DJANGO_CACHE_LOCATION', default='redis://redis:6379/1'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}


# ------------------------------------------------------------------------------
# DJANGO REST FRAMEWORK Configuration
# http://www.django-rest-framework.org/api-guide/versioning/#acceptheaderversioning
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
}

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', ],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', ],
            'level': 'ERROR',
            'propagate': True
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'mail_admins', ],
            'propagate': True
        }
    }
}
