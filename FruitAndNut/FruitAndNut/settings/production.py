from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD']
    }
}


STATIC_ROOT = os.path.join(os.environ['HOME'], 'Assets/FruitAndNut/static')
MEDIA_ROOT = os.path.join(os.environ['HOME'], 'Assets/FruitAndNut/media')
