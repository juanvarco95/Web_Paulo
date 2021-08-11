from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DB_Paulo_WEB',
        'USER' : 'postgres',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432'
    }
}

