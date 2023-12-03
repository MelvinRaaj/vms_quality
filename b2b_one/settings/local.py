import environ
import os
from settings.common import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

# Set the project base directory
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['127.0.0.1', '.127.0.0.1' , 'localhost',  '.localhost']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),
        'NAME': BASE_DIR / env('DBNAME'),
    }
}

#email
EMAIL_FROM = os.environ.get('AUTHEMAIL_DEFAULT_EMAIL_FROM') or 'melvin@myaccsellerate.com'
EMAIL_BCC = os.environ.get('AUTHEMAIL_DEFAULT_EMAIL_BCC') or 'melvin@myaccsellerate.com'

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = 587
EMAIL_HOST_USER = "postmaster@sandboxcfa091738a7f4dd181d4f4a658fb7a77.mailgun.org"
EMAIL_HOST_PASSWORD = "3e85f028b647ee0719df5c94d956a006-09001d55-03330050"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False