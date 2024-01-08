import environ
import os

from pathlib import Path
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


# SECURITY WARNING: don't run with debug turned on in production!
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
env.read_env(os.path.join(BASE_DIR, 'oc_lettings_site', '.env'))
# environ.Env.read_env(os.path.join(BASE_DIR, 'oc_lettings_site', '.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*', ]

# Application definition

INSTALLED_APPS = [
    'oc_lettings_site.apps.OCLettingsSiteConfig',
    'common.apps.CommonConfig',
    'lettings.apps.LettingsConfig',
    'profiles.apps.ProfilesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oc_lettings_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASE_URL = env('DATABASE_URL')
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    # The db() method is an alias for db_url().
    'default': env.db(var=env('DATABASE_URL'), default=env('DATABASE_URL'), engine=env('ENGINE')),
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static', ]

# set up sentry
sentry_sdk.init(
    dsn=env('SENTRY_DSN'),
    enable_tracing=True,  # monitor performance
    send_default_pii=True,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    integrations=[
        DjangoIntegration(
            transaction_style='url',
        )
    ]
)

# LOGGING
LOG_DIR = os.path.join(BASE_DIR, 'log')
LOG_FILE_MAIN = 'main.log'
LOG_FILE_DJANGO = 'django.log'
LOG_PATH_DJANGO = os.path.join(BASE_DIR, LOG_FILE_DJANGO)
LOG_PATH_MAIN = os.path.join(BASE_DIR, LOG_FILE_MAIN)

if not os.path.exists(LOG_DIR):
    try:
        os.mkdir(LOG_DIR)
    except FileExistsError:
        pass

if not os.path.exists(LOG_PATH_DJANGO):
    f = open(LOG_PATH_DJANGO, 'a').close()
if not os.path.exists(LOG_PATH_MAIN):
    f = open(LOG_PATH_MAIN, 'a').close()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'semi_verbose': {
            'format': '%(asctime)s [%(levelname)s] %(funcName)s(): %(message)s'
        },
        'verbose': {
            'format': '%(asctime)s [%(levelname)s] %(module)s %(name)s (line %(lineno)d) %(funcName)s(): %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': f'{BASE_DIR}/log/django.log',
            'formatter': 'verbose'
        },
        'main_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': f'{BASE_DIR}/log/main.log',
            'formatter': 'semi_verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django_log'],
            'level': 'INFO',
        },
        'main': {
            'handlers': ['main_log'],
            'level': 'INFO',
        },
    }
}
