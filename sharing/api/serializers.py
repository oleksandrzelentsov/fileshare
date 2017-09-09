from rest_framework.serializers import ModelSerializer

from sharing.models import ShareableFile


class ShareableFileListSerializer(ModelSerializer):
    class Meta:
        model = ShareableFile
        fields = [
            'id',
            'name',
            'get_raw_url',
            'public',
        ]


class ShareableFileDetailSerializer(ModelSerializer):
    class Meta:
        model = ShareableFile
        fields = [
            'id',
            'name',
            'get_raw_url',
            'public',
        ]