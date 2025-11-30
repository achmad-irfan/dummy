from .base import *

DEBUG= False

ALLOWED_HOSTS = ['www.achmad-irfan.my.id','achmad-irfan.my.id']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

STATIC_ROOT = "/home/wwwachm1/public_html/portfolio_static"
MEDIA_ROOT = '/home/wwwachm1/public_html/portfolio_media'