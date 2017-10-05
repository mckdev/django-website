import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '11)dkff6!#acz&qvuy)v42jkap@_94e)o#xc)2jyzsi0w7p8dn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'cms.apps.CmsConfig',
    'portfolio.apps.PortfolioConfig',
    'gallery.apps.GalleryConfig',
    'uploads.apps.UploadsConfig',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'constance',
    'constance.backends.database',
    'ckeditor',
    'ckeditor_uploader',
    'django_countries',
    'easy_thumbnails',
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

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'constance.context_processors.config',
                'cms.context_processors.menu_processor',
                'cms.context_processors.footer_processor',
                'gallery.context_processors.gallery_categories_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# CKEditor

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Maximize', 'Format', 'Bold', 'Italic', 'Underline', '-', 'TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor', 'Image', 'Embed', '-'],
            ['Undo', 'Redo', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo', 'Find', 'Replace', '-', 'SelectAll', '-', 'Source']
        ],
        'height': 400,
        'width': '100%',
        'extraPlugins': ','.join(
            [
                'image2',
                'embed',
            ]),
        'language': 'en',
    },

}


# Email server configuration
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_USE_TLS = True
    EMAIL_HOST = ''  # E.g. smtp.gmail.com
    EMAIL_HOST_USER = ''  # E.g. user@gmail.com
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = 587


# Authentication backend
AUTHENTICATION_BACKENDS = ('accounts.backends.CustomModelBackend', )


# Custom dynamic settings with Constance
# https://django-constance.readthedocs.io/en/latest/

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'SITE_TITLE': ('Django website', 'Descriptive title of the website.'),
    'HOMEPAGE_ID': (1, 'Homepage ID, '
                       'After creating a homepage, type in the ID here.'),
    'TOPMENU_ID': (1, 'Top menu ID, '
                       'After creating a menu, type in the ID here.'),
    'FOOTER_ID': (1, 'Site footer ID, '
                      'After creating a footer, type in the ID here.'),
    'FACEBOOK_URL': ('', 'Link to your Facebook page.'),
    'TWITTER_URL': ('', 'Link to your Twitter profile.'),
    'GPLUS_URL': ('', 'Link to your Google+ profile.'),
    'YOUTUBE_URL': ('', 'Link to your YouTube page.'),
    'VIMEO_URL': ('', 'Link to your Vimeo page.'),
    'LINKEDIN_URL': ('', 'Link to your LinkedIn profile.'),
    'GALLERY_DESCRIPTION': ('', 'Shot description of gallery index page.'),
    'PORTFOLIO_ENABLED': (True, 'Enable or diable the portfolio', bool),
}

# easy_thumbnails

THUMBNAIL_ALIASES = {
    '': {
        'thumbnail': {'size': (250, 250), 'crop': True},
    },
}