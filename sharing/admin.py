from django.contrib import admin

import sharing
from sharing.models import ShareableFile

admin.site.register(ShareableFile)
