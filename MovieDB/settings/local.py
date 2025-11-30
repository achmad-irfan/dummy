from .base import *

DEBUG= True

ALLOWED_HOSTS = []




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME_LOKAL'),
        'USER': config('DB_USER_LOKAL'),
        'PASSWORD': config('DB_PASSWORD_LOKAL'),
        'HOST': config('DB_HOST_LOKAL'),
        'PORT': config('DB_PORT_LOKAL'),
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')]
