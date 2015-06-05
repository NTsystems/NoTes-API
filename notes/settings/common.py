"""Contains common project settings."""
import os

# local project paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(PROJECT_ROOT)

# application security
AUTH_USER_MODEL = "account.User"
SECRET_KEY = 'kx#h^c4%-gunm6d9ekp+kjkb$yeu6hc%oe6y19)r&w8z1)qatj'
ALLOWED_HOSTS = ["*"]

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
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',

    'djcelery',

    'notes.apps.account',
    'notes.apps.writer',
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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '1.0.0',
    'api_path': '/',
    'enabled_methods': ['get', 'post', 'put', 'delete'],
    'api_key': 'bbc7f7b5492468db6a4a54a00c1b504930371792',
    'is_authenticated': False,
    'is_superuser': False,
    'permission_denied_handler': None,
    'info': {
        'contact': 'office@ntsystems.rs',
        'description': 'NT notes active API documentation.',
        'license': 'MIT',
        'licenseUrl': 'http://opensource.org/licenses/MIT',
        'title': 'NoTes',
    },
    'doc_expansion': 'none',
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
STATIC_ROOT = os.path.join(REPO_ROOT, 'assets')

# rabbitmq is default broker
BROKER_URL = 'amqp://admin:mypass@localhost:5672/'

CELERY_RESULT_BACKEND = 'amqp://admin:mypass@localhost:5672/'

CELERY_TASK_SERIALIZER = 'json'

# email configuration (gmail)
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'testntsystems'
EMAIL_HOST_PASSWORD = 'testiranje'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'testntsystems@gmail.com'