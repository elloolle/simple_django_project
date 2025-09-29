from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ...models import Image, Text, Video
from ..serializers import TextSerializer, ImageSerializer, VideoSerializer
from ..services.AwsService import uploadFile
from ..services.ModeratorService import moderateImage, moderateText, moderateVideo


class TextModeratorView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Text.objects.all()
    serializer_class = TextSerializer

    def perform_create(self, serializer):
        text = serializer.save(author=self.request.user)
        moderateText.delay(text)


class ImageModeratorView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        image = serializer.save(author=self.request.user)
        image_file = image.image_file
        uploadFile.delay(image_file.path, image_file.name)
        # moderateImage.delay(image)


class VideoModeratorView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
        video = serializer.save(author=self.request.user)
        video_file = video.video_file
        uploadFile.delay(video_file.path, video_file.name)
        moderateVideo.delay(video)
