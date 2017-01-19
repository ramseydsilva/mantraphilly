import os, sys, environ

root = environ.Path(__file__) - 2
PROJECT_ROOT = sys.prefix
PROJECT_PATH = root()
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env(os.path.join(PROJECT_ROOT, 'config/site.conf'))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3u585o#-)on1kdx15(ht(&mrs11ezjwf#yy=^6lh&w$&*k*0al'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'server.home',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_PATH, 'templates')
        ],
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

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Custom settings here

CONFIG_BUILD_DIR = os.path.join(PROJECT_ROOT, 'config')
CONFIG_TEMPLATE_DIR = os.path.join(PROJECT_PATH, 'templates/config')

PROJECT_NAME = 'mantra'
BASE_URL = env('BASE_URL', default="")
STATIC_URL = BASE_URL + env('STATIC_URL', default='/static/')
STATIC_URL_ = STATIC_URL[:-1]
DOCS_URL = BASE_URL + env("DOCS_URL", default="/docs")
API_ROOT = BASE_URL + env('API_ROOT', default="/api")
MEDIA_URL = BASE_URL[1:] + env('MEDIA_URL', default='/media/')
MEDIA_URL_ = MEDIA_URL[:-1]
if not BASE_URL: BASE_URL = "/"

DATA_ROOT = os.path.join(PROJECT_ROOT, "data")
MEDIA_ROOT = DATA_ROOT
STATIC_ROOT = os.path.join(PROJECT_ROOT, "src/web/web")
DOCS_ROOT = env("DOCS_ROOT", default=os.path.join(PROJECT_ROOT, "src/docs/build/html"))
STATICFILES_DIRS = []

PROCESSES = env("PROCESSES", default=['mantra'], cast=list)
SUPERVISOR_PATH = env("SUPERVISOR_PATH", default="/etc/supervisor/conf.d/%s.conf" %(PROJECT_NAME))
NGINX_PATH = env("NGINX_PATH", default="/etc/nginx/sites-enabled/%s" %(PROJECT_NAME))
UWSGI_PATH = env("UWSGI_PATH", default="/etc/uwsgi/sites-enabled/%s.ini" %(PROJECT_NAME))
WEBSERVER = 'nginx'
RUN_AS_USER = 'ramsey'
UWSGI_SOCK = '/tmp/%s.sock' %(PROJECT_NAME)
UWSGI_BIN = env("UWSGI_BIN", default=os.path.join(PROJECT_ROOT, 'bin/uwsgi'))
ALLOWED_HOSTS = env('ALLOWED_HOSTS', default=[], cast=[str])
if len(ALLOWED_HOSTS):
    SERVER_NAME = ALLOWED_HOSTS[0]
else:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
    SERVER_NAME = '%s.local' %(PROJECT_NAME)

