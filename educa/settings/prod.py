from decouple import config

from .base import *

DEBUG = True

ADMINS = [
    ('shen', 'shenleekhalid@gmail.com'),
]

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'educa.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
