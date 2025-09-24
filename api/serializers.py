from rest_framework import serializers

from .models import Image, Text, User, Video


# class RecipeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recipe
#         fields = '__all__'
class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"