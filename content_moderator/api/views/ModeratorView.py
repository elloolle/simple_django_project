from django.views import View
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ...models import Image
from ..serializers import ImageSerializer
from ..services.AwsService import AwsService
from ..services.ModeratorService import ModeratorService

AwsService = AwsService()
ModeratorService = ModeratorService()


class ImageModeratorView(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    def perform_create(self, serializer):
        image = serializer.save()
        ModeratorService.moderateImage(image)