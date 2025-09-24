from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Text, Image, Video
from .serializers import RecipeSerializer

# Create your views here.
# class RecipeView(ModelViewSet):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
