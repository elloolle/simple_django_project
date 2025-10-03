from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ...models import Image, Text, Video
from ..serializers import ImageSerializer, TextSerializer, VideoSerializer
from content_moderator.services.AwsService import uploadFile
from content_moderator.services.ModeratorService import moderateImage, moderateText, moderateVideo


class TextModeratorView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Text.objects.all()
    serializer_class = TextSerializer

    def perform_create(self, serializer):
        text = serializer.save(author=self.request.user)
        moderateText.delay(text)

class BaseContentModerator(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = None
    moderate_task = None
    serializer_class = None
    def perform_create(self, serializer):
        content = serializer.save(author=self.request.user)
        content_file = content.content_file
        uploadFile.delay(content_file.path, content_file.name)
        self.moderate_task.delay(content.id)

class ImageModeratorView(BaseContentModerator):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    moderate_task = moderateImage

class VideoModeratorView(BaseContentModerator):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    moderate_task = moderateVideo
