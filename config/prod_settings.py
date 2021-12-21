from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-9p_u9hgrn(^k5nmn+dgfniovbg673-dvf&nty2l+0b8j^n1t'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

from getpass import getpass
	
DATABASES = {
	'default': {
	    'ENGINE': 'django.db.postgresql_psycopg2', 
	    'NAME': 'storage',
	    'USER': 'userdb',
	    'PASSWORD': '123456',
	    'HOST': 'localhost',
		'PORT':'5432',
	    }
}

STATIC_DIR = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR,'static')