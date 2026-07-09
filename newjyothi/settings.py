"""
Django settings for newjyothi project — NEW JYOTHI VASTRALAYAM saree shop.
"""

from pathlib import Path
import os
import dj_database_url
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-newjyothi-vastralayam-secret-key-change-in-production-987654321'

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    "cloudinary",
    "cloudinary_storage",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'newjyothi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processors.shop_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'newjyothi.wsgi.application'

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("postgresql://newjyothi_user:JAh2PD6NLyT3cQbYPX1zDKG7K2IjzGIJ@dpg-d93ra1u7r5hc73dkcnfg-a/newjyothi")
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/dashboard/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/dashboard/login/'

# ---- Shop business details (used across templates) ----
SHOP_NAME = 'JYOTHI SHOPPING MALL'
SHOP_PHONE = '9030459651'
SHOP_WHATSAPP = '919533813859'  # with country code, no +
SHOP_ADDRESS = 'Bodrai Bazar, Nakerkal, Nalgonda.'
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "eh9au0lu",
    "API_KEY": "659273258344362",
    "API_SECRET": "PRNtDHha-8OzKhrb7f4gZbNtkUo",
}
