# -*- encoding: utf-8 -*-
import dj_database_url
import os

""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Árbol de Directorios
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates')
]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Administracion
"""
ADMINS = (
    ('Martin Josemaria', 'martin.vuelta@gmail.com'),
    ('Fernanda Hereña', 'fernandaflorezherena@gmail.com'),
)


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Seguridad
"""
SECRET_KEY = os.environ['IZANAASTEROID_SECRET_KEY']

if os.environ['I_AM_ON_HEROKU'] == 'True':
    DEBUG = False
    TEMPLATE_DEBUG = False
else:
    DEBUG = True
    TEMPLATE_DEBUG = True


ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

APPEND_SLASH = True


# Application definition

INSTALLED_APPS = (
    # Skin (Third party)
    'suit',

    # Default Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'captcha',
    'ckeditor',

    # APIs
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'IzanaAsteroid.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'IzanaAsteroid.wsgi.application'

""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Bases de datos
"""
if os.environ['I_AM_ON_HEROKU'] == 'True':
    DATABASES = {
        'default': dj_database_url.config(),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'izanaasteroiddb',
            'USER': 'izana',
            'PASSWORD': os.environ['IZANAASTEROID_DB_KEY'],
            'HOST': '127.0.0.1',
            'PORT': '',
        }
    }


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Internationalization
"""
LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Otros ajustes
"""
# Google Maps API key
GOOGLE_MAPS_API_KEY = 'AIzaSyBVyXTW7aLXoUrrBDOcGmamqEzauBQHVy8'

# Configuracion de django-suit
SUIT_CONFIG = {
    'ADMIN_NAME': 'IzanaAsteroid | SoftButterfly',
    'MENU_OPEN_FIRST_CHILD': False,
}

# ckeditor
CKEDITOR_UPLOAD_PATH = "ckeditor/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = '/static/js/jquery-1.11.2.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'height': 300,
        'width': 450,
    },
}

# reCaptcha
RECAPTCHA_PUBLIC_KEY = '6LcGMgUTAAAAAM6pkdXTm71-S_wC36eY7jtT2E3j'
RECAPTCHA_PRIVATE_KEY = os.environ['IZANAASTEROID_RECAPTCHA_PRIVATE_KEY']
RECAPTCHA_USE_SSL = True
