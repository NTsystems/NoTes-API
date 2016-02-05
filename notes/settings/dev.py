"""Contains development settings."""
from notes.settings.common import *


DEBUG = True


#
# Storage
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'ntsystems',
        'PASSWORD': 'ntsystems',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
