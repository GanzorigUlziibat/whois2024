import psycopg2
import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-2am@_6ixr33atxv4hyl+^6r3%*xboew+vcoy2bgpr!v)8z8mdw'
DEBUG = True
ALLOWED_HOSTS = ["*", "localhost", "192.168.4.102"]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whois_app',
    'corsheaders',
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

ROOT_URLCONF = 'whois.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'whois.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

WSGI_APPLICATION = 'whois.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = 'static/'
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


def connectDB():
    con = psycopg2.connect(
        # host='192.168.0.15',  # dotood
        host='59.153.86.254',# gadaad
        dbname='qrlesson',
        user='userlesson',
        password='123',
        port='5938',
    )
    return con
# connectDB


def disconnectDB(con):
    con.close()
# disconnectDB


def sendResponse(statusCode, data=[], action=''):
    resJson = {}
    resJson['action'] = action
    resJson['resultCode'] = statusCode
    resJson['resultMessage'] = statusMessage[statusCode]
    resJson['data'] = data
    resJson['size'] = len(data)
    resJson['curDate'] = datetime.now().strftime('%Y/%m/%d %T')
    return resJson


statusMessage = {
    200: 'Success',
    204: 'No Content',
    301: "Bad request",
    404: "Not found",
    405: 'Invalid Method',
    4001: 'Invalid Json',
    4002: 'Action Missing',
    4003: 'Invalid Action',
    5000: 'Server Error',
}
