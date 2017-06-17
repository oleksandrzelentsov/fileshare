import os

from django.contrib.auth.models import User
from django.db import models
from django.db.models import FileField

from files.settings import UPLOADED_FILES_DIR


class ShareableFile(models.Model):
    file = FileField(upload_to=UPLOADED_FILES_DIR)
    user = models.ForeignKey(User)

    def __str__(self):
        filename = os.path.basename(self.file.name)
        return "[{user}] {filename}".format(
            user=self.user.get_username(),
            filename=filename,
        )
