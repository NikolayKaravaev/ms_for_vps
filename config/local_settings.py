from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-9p_u9hgrn(^k5nmn+weee9bo7!u+5z3-dvf&nty2l+0b8j^n1t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

from getpass import getpass
	
DATABASES = {
	'default': {
	    'ENGINE': 'django.db.backends.mysql', 
	    'NAME': 'storage',
	    'USER': 'root',
	    'PASSWORD': '007hamSTER1980!',
	    'HOST': 'localhost',
	    }
}


STATIC_DIR = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [STATIC_DIR]