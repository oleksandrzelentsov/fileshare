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


class ShareableFileCreateSerializer(ModelSerializer):
    class Meta:
        model = ShareableFile
        read_only_fields = ('user', )
        fields = [
            'file',
            'user',
            'public',
        ]
