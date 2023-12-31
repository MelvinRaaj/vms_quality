"""
Django settings for b2b_one project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

# settings.py was changed based on https://thinkster.io/tutorials/configuring-django-settings-for-production


from pathlib import Path
import environ
import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    
    #added for allauth
    'django.contrib.sites',
    
    #3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'invitations',
    'rest_framework',
    'django_filters',
    'drf_spectacular',
    'crispy_forms',
    'crispy_bootstrap5', 
    'phonenumber_field',
    
    #B2B_One
    'tenant',
    'users',
    'invitation',
    'landing',
    'api',
    'home',
    'department',
    'product_collections',
    'design_spec',
    'demo',
    'quality',
    'quality2',
    'products',
    'shopping_list',
    'materials',
    'rfi',
    'samples',
    
]


AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

# ************** allauth settings ******************

SITE_ID = 1

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_UNIQUE_EMAIL = True


AUTH_USER_MODEL = 'users.CustomUser'


ACCOUNT_EMAIL_VERIFICATION='mandatory'

# ACCOUNT_CONFIRM_EMAIL_ON_GET=True
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_PHONE_VERIFICATION_METHOD = 'sms'

ACCOUNT_ADAPTER = 'users.adapter.UserAccountAdapter'


# ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.CustomUserCreationForm'

# Email confirmation
ACCOUNT_EMAIL_SUBJECT_PREFIX = "B2B_One"
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# After 10 failed login attempts, restrict logins for 30 minutes
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 1800
ACCOUNT_PASSWORD_MIN_LENGTH = 3

# Other settings
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
SOCIALACCOUNT_AUTO_SIGNUP = False

LOGIN_REDIRECT_URL='home:home_page'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL='home:home_page'
LOGOUT_REDIRECT_URL = '/'

# ************** django-invitations settings ******************

# INVITATIONS_ADAPTER ='invitation.adapter.InviteAdapter'

INVITATIONS_SIGNUP_REDIRECT ='signup_invite'

INVITATIONS_INVITATION_MODEL='invitation.CustomInvitation'

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }


#3rd party app dependancies

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

#breadcrumb
BREADCRUMBS_TEMPLATE = "view_breadcrumbs/bootstrap5.html"

BREADCRUMBS_HOME_LABEL = "Home"


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
   
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'b2b_one.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR /"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                 # `allauth` needs this from django
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'b2b_one.wsgi.application'

DATE_INPUT_FORMATS = ['%d-%m-%Y']


#email setup
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = 587
EMAIL_HOST_USER = "postmaster@sandboxcfa091738a7f4dd181d4f4a658fb7a77.mailgun.org"
EMAIL_HOST_PASSWORD = "3e85f028b647ee0719df5c94d956a006-09001d55-03330050"
EMAIL_USE_TLS = True


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [

    BASE_DIR / "static",
    #boostrap
    BASE_DIR / "boot"

]


STATIC_ROOT = "static_root"

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"#add this line

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings for drf-spectacular -swagger integration for python
SPECTACULAR_SETTINGS = {

    'TITLE': 'B2B_One API',
    'DESCRIPTION': 'API Builder',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS

    # available SwaggerUI configuration parameters
    # https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True,
    },
    # available SwaggerUI versions: https://github.com/swagger-api/swagger-ui/releases
    "SWAGGER_UI_DIST": "//unpkg.com/swagger-ui-dist@3.35.1", # default
    "SWAGGER_UI_FAVICON_HREF": STATIC_URL + "logo.png", # default is swagger favicon
}


