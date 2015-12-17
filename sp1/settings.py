import os
from saml_config import get_saml_config

from common_settings import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGOUT_REDIRECT_URL = "/accounts/profile"

DEBUG = False

ALLOWED_HOSTS = [HOSTNAME]

if DEBUG:
	ROOT_URL = "http://" + HOSTNAME + ":8000"
else:
	ROOT_URL = "http://" + HOSTNAME

SAML_CONFIG = get_saml_config(ROOT_URL, BASE_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '123123123'


INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'djangosaml2',
	'sp1'
)

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'djangosaml2.backends.Saml2Backend',
)

LOGIN_URL = '/saml2/login/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

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

ROOT_URLCONF = 'sp1.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
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

WSGI_APPLICATION = 'sp1.wsgi.application'


DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, SQLITE_DB_PATH),
	}
}


LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
                'standard': {
                        'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
                },
        },
        'handlers': {
                'django_request': {
                        'level': 'DEBUG',
                        'class': 'logging.handlers.RotatingFileHandler',
                        'filename': LOG_PATH,
                        'maxBytes': 1024*1024*5,
                        'backupCount': 5,
                        'formatter':'standard',
                },

        },
        'loggers': {
                'django.request': {
                        'handlers': ['django_request'],
                        'propagate': True
                },
        },
		'root': {
			'handlers': ['django_request'],
			'level': 'DEBUG'
		},
}



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
