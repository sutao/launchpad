import os


#
# Debug or not
#
DEBUG = True
VERSION = 1.0


#
# Basic settings
#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = '@tf30izrq^m@&gw%6yqxkn=9@v2e2sgm(&s46r#23euqz*f#fn'
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'launchpad.urls'
WSGI_APPLICATION = 'launchpad.wsgi.application'
SITE_ID = 1


#
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
#
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


#
# CORS Whitelist
#
CORS_ORIGIN_ALLOW_ALL = True


#
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev-db.sqlite3'),
    }
}


# ---------------------------------------------------------
# Static options across all environments
# ---------------------------------------------------------


#
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# The settings below is a workaround for Elastic Beanstalk's static serving
#
STATIC_ROOT = os.path.join(BASE_DIR,'djangostatic/')
STATIC_URL = '/djangostatic/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


#
# Application definition
#
INSTALLED_APPS = [
    'launchpad',
    'grappelli',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_framework_swagger',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'brightbrain/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]


#
# Authentication Backends
#
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


#
# API settings
#
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}


#
# Misc settings
#
GRAPPELLI_ADMIN_TITLE = 'Launchpad Admin'
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')