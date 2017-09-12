from files.base_settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('FILESHARE_DB_NAME'),
        'USER': os.environ.get('FILESHARE_DB_USER'),
        'PASSWORD': os.environ.get('FILESHARE_DB_PASSWORD'),
        'HOST': os.environ.get('FILESHARE_DB_HOST'),
        'PORT': os.environ.get('FILESHARE_DB_PORT'),
    }
}
