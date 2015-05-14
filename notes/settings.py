"""Contains notes project settings."""
import os

# Development mode?
DEBUG = os.environ.get("DEBUG", True)

# local project paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(PROJECT_ROOT)

# application security
AUTH_USER_MODEL = "account.User"
SECRET_KEY = 'kx#h^c4%-gunm6d9ekp+kjkb$yeu6hc%oe6y19)r&w8z1)qatj'
ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0"]

# application definition
ROOT_URLCONF = 'notes.urls'
WSGI_APPLICATION = 'notes.wsgi.application'

#
# dependencies
#
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notes.apps.account',
    'notes.apps.writer',
    'rest_framework',
    'rest_framework.authtoken',
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

#
# storage
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'ntsystems',
        'PASSWORD': 'ntsystems',
        'HOST': '0.0.0.0',
        'PORT': '5432'
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# default language
LANGUAGE_CODE = 'en-us'

# formatting (activate int. support, date/time etc.)
USE_I18N = True
USE_L10N = True

# timezone awareness
USE_TZ = True
TIME_ZONE = 'UTC'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# logging (TBD)
