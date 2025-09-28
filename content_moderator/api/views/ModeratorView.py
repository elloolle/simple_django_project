from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ...models import Image
from ..serializers import ImageSerializer
from ..services.AwsService import AwsService
from ..services.ModeratorService import ModeratorService

AwsService = AwsService()
ModeratorService = ModeratorService()


class ImageModeratorView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        image = serializer.save()
        ModeratorService.moderateImage(image)
