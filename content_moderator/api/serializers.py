from rest_framework import serializers

from ..models import Image, Text, User, Video


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
