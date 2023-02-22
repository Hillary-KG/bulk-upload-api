from rest_framework import serializers
from .models import UserRecord, FileObject


class UploadSerializer(serializers.Serializer):
    """
    serializer class for a file upload
    """

    file = serializers.FileField()

    class Meta:
        fields = ["file"]


class UserRecordSerializer(serializers.ModelSerializer):
    """
    serializer class for the user record as extracted from the file
    """

    class Meta:
        model = UserRecord
        fields = "__all__"


class FileObjectSerializer(serializers.ModelSerializer):
    """
    serializer classs for the file object
    """

    class Meta:
        model = FileObject
        fieds = "__all__"

        extra_kwargs = {"status": {"read_only": True}}
