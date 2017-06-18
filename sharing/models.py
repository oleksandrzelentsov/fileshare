import os
import hashlib

from django.contrib.auth.models import User
from django.db import models
from django.db.models import FileField, CharField
from django.urls import reverse

from files.settings import UPLOADED_FILES_DIR


class ShareableFile(models.Model):
    file = FileField(upload_to=UPLOADED_FILES_DIR)
    name = CharField(max_length=64)
    hash = CharField(max_length=40, unique=True, blank=True)
    user = models.ForeignKey(User)
    public = models.BooleanField(default=False)

    def __str__(self):
        return "[{user} {hash}] {filename}".format(
            user=self.user.get_username(),
            filename=self.name,
            hash=self.hash,
        )

    def compute_hash(self):
        hash_str = '{id}{filename}'.format(
            id=self.id,
            filename=self.name,
        ).encode()
        return hashlib.sha1(hash_str).hexdigest()

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = os.path.basename(self.file.name)
        if not self.hash:
            self.hash = self.compute_hash()
        return super(ShareableFile, self).save(*args, **kwargs)

    def get_raw_url(self):
        return reverse('raw', kwargs={'file_hash': self.hash})
