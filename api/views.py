from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Text, Image, Video
from .serializers import TextSerializer, ImageSerializer, VideoSerializer

# Create your views here.
# class RecipeView(ModelViewSet):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
class TextView(ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
class ImageView(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
class VideoView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer