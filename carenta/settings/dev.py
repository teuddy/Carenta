from .base import * 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'carentadb',
        'USER': 'postgres',
        'PASSWORD': '9207teuddy',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

SECRET_KEY = 'abc'

DEBUG = True

ALLOWED_HOSTS = ['*']