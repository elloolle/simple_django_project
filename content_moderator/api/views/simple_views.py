from rest_framework.viewsets import ModelViewSet

from ...models import Image, Text, Video
from ..serializers import ImageSerializer, TextSerializer, VideoSerializer


class TextView(ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer


class ImageView(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class VideoView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

