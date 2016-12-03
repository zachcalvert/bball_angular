import os
import environ

project_root = environ.Path(__file__) - 3  
env = environ.Env(DEBUG=(bool, False),)  
CURRENT_ENV = 'dev' # 'dev' is the default environment

# read the .env file associated with the settings that're loaded
env.read_env('./fantasy_bball/{}.env'.format(CURRENT_ENV))  

SECRET_KEY = env('SECRET_KEY')  
DEBUG = env('DEBUG')  

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, '../assets'), # react frontend assets
    os.path.join(BASE_DIR, '../static'), # django frontend assets
)

STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, '../../staticfiles'))

STATIC_URL = '/static/'  

STATICFILES_FINDERS = [  
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, '../webpack-stats.json'),
    }
}


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'rest_framework',
    'webpack_loader',

    'leagues',
    'players',
    'schedule',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fantasy_bball.urls'  

TEMPLATES = [  
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['leagues'],
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