from files.base_settings import *


DATABASES = {'default': dj_database_url.config(default=os.environ["DATABASE_URL"])}
