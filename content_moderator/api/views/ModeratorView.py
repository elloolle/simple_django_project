from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ...models import Image, Text, Video
from ..serializers import ImageSerializer, TextSerializer, VideoSerializer
from ..services.AwsService import uploadFile
from ..services.ModeratorService import moderateImage, moderateText, moderateVideo


class TextModeratorView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Text.objects.all()
    serializer_class = TextSerializer

    def perform_create(self, serializer):
        text = serializer.save(author=self.request.user)
        moderateText.delay(text)


def contentModeratorViewGenerator(model, modelSerializer, moderateContent):
    class ContentModeratorView(ModelViewSet):
        permission_classes = [IsAuthenticated]
        queryset = model.objects.all()
        serializer_class = modelSerializer

        def perform_create(self, serializer):
            content = serializer.save(author=self.request.user)
            content_file = content.content_file
            uploadFile.delay(content_file.path, content_file.name)
            moderateContent.delay(content.id)

    return ContentModeratorView


ImageModeratorView = contentModeratorViewGenerator(
    Image, ImageSerializer, moderateImage
)
VideoModeratorView = contentModeratorViewGenerator(
    Video, VideoSerializer, moderateVideo
)
