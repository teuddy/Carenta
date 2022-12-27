import django_on_heroku
from decouple import config

from dotenv import find_dotenv, load_dotenv


from .base import * 

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']


load_dotenv(find_dotenv())

DATABASES = {'default': dj_database_url.config(default='sqlite:///db.sqlite3',conn_max_age=600,ssl_require=False)}



DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[% (asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level':'DEBUG',
            'class':  'logging. StreamHandler',
             },
        },
        'loggers': {
            'MYAPP':{
                'handlers': ['console'],
                'level': 'DEBUG'
            },
    }
}

# heroku settings 
django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']