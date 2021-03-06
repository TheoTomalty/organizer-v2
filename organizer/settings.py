import os

DEBUG = True
TEMPLATE_DEBUG = True

# Server setup
ALLOWED_HOSTS = ['organizer.theo.tomalty.com', 'localhost']
SECRET_KEY = 'l=l4zuuyp@x(*)ki)vo6q0n%$hw@$b93b7jhe8!ajabf(*kv=e'

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.auth',
]

MIDDLEWARE = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Pointing to files/directories
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir)
ROOT_URLCONF = "organizer.urls"

# Database
import dj_database_url
DATABASES = {'default': dj_database_url.config()}

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'organizer/templates')],
    },
]

# Static files
STATIC_URL = '/build/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "build"),
]