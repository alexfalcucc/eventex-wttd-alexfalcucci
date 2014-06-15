"""
Django settings for eventex project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/
--- a/eventex/settings.py
+++ b/eventex/settings.py
@@ -8,9 +8,8 @@ For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from decouple import config
from dj_database_url import parse as db_url
from unipath import Path
BASE_DIR = Path(__file__).parent
import dj_database_url


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['.localhost','127.0.0.1','.herokuapp.com']

#para ligar e desligar, consecutivamete:
#heroku config:set DEBUG=True
#heroku config:set DEBUG=False


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # dispositivos
    'bootstrapform',
    #'south',
    # apps
    'eventex.core',
    'eventex.subscriptions',
    "eventex.myauth",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eventex.urls'

WSGI_APPLICATION = 'eventex.wsgi.application'

#MANAGER
# alias manage='python $VIRTUAL_ENV/manage.py'

# Usar o South para preparar o banco nos testes? True: sim. (default) - False: naoo! USE O syncdb.

SOUTH_TESTS_MIGRATE = False


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
'''
"""@@ -58,7 +57,7 @@ WSGI_APPLICATION = 'eventex.wsgi.application'"""
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': BASE_DIR.child('db.sqlite3'),
        }
}'''

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
        cast=db_url),

}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR.child('staticfiles')

STATIC_URL = '/static/'


# Refatorando com Custom User
"""
AUTHENTICATION_BECKENDS = (
    'eventex.myauth.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)"""

AUTH_USER_MODEL='myauth.User'