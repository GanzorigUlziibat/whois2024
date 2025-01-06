import psycopg2
import json
import smtplib
from pathlib import Path
from datetime import datetime
from email.mime.text import MIMEText


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-2am@_6ixr33atxv4hyl+^6r3%*xboew+vcoy2bgpr!v)8z8mdw'
DEBUG = True

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

WSGI_APPLICATION = 'whois.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = 'static/'
CORS_ORIGIN_ALLOW_ALL = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ALLOWED_HOSTS = ['whoism.mandakh.org', '127.0.0.1']


def connectDB():
    con = psycopg2.connect(
        host='192.168.0.15',  # dotood
        # host='59.153.86.254',  # gadaad
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


def sendResponse(statusCode, data=[], action=None):
    resJson = {}
    resJson['action'] = action
    resJson['resultCode'] = statusCode
    resJson['resultMessage'] = statusMessage[statusCode]
    resJson['data'] = data
    resJson['size'] = len(data)
    resJson['curDate'] = datetime.now().strftime('%Y/%m/%d %T')
    return resJson


statusMessage = {
    1000: 'Бүртгэлтэй хэрэглэгч байна',
    1001: 'Token-ний хугацаа дууссан эсвэл хүчингүй token байна',
    1002: 'Баталгаажсан хэрэглэгч байна',
    1003: 'Амжилттай, Та мэйл хаягруугаа орж бүртгэлээ баталгаажуулга уу!',
    1004: 'Бүртгэлгүй хэрэглэгч байна',


    200: 'Success',
    204: 'No Content',
    301: "Bad request",

    404: "Not found",
    405: 'Invalid Method',
    4001: 'Invalid Json',
    4002: 'Action Missing',
    4003: 'Invalid Action',
    4004: 'Register Service Key дутуу',
    4005: 'Database Error',
    4006: 'Login key Error',
    4007: 'Нууц үг буруу байна',
    4008: 'Бүртгэлээ баталгаажуулна уу',

    5000: 'Server Error',
    5001: 'login Service дотоод алдаа',
    5004: 'Register Service дотоод алдаа',
}


def sendMail(recipient, subj, bodyHtml):
    sender_email = "testmail@mandakh.edu.mn"
    sender_password = "Mandakh2"
    recipient_email = recipient
    subject = subj
    body = bodyHtml

    html_message = MIMEText(body, 'html')
    html_message['Subject'] = subject
    html_message['From'] = sender_email
    html_message['To'] = recipient_email
    with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email,
                        html_message.as_string())
        server.quit()
# sendMail
