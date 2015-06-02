"""Production settings."""
from notes.settings.common import *


DEBUG = False


#
# Storage
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'ntsystems',
        'PASSWORD': 'ntsystems',
        'HOST': os.getenv("POSTGRES_PORT_5432_TCP_ADDR"),
        'PORT': os.getenv("POSTGRES_PORT_5432_TCP_PORT")
    }
}
