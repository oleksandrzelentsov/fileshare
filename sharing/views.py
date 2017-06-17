from django.http import Http404
from django.views import View

from sharing.models import ShareableFile


class FileView(View):
    def get(self, request, file_hash):
        try:
            obj = ShareableFile.objects.get(hash=file_hash)
        except ShareableFile.DoesNotExist:
            return Http404
        if obj.user != request.user:
            return Http404
        return obj.file
