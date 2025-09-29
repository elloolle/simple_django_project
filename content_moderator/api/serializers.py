from rest_framework import serializers

from ..models import Image, Text, User, Video
from .services.AwsService import generatePrinsignedURL




class ContentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")


class TextSerializer(ContentSerializer):
    class Meta:
        model = Text
        fields = "__all__"


class ImageSerializer(ContentSerializer):
    class Meta:
        model = Image
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["image_file"] = generatePrinsignedURL(instance.image_file.name)
        return rep


class VideoSerializer(ContentSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password"]

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )
