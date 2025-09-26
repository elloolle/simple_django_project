from django.views import View
from rest_framework import status
from rest_framework.response import Response

from ..serializers import ImageSerializer
from ..services.AWS_service import AWS_service

AWS_service = AWS_service()


class ImageModeratorView(View):
    def get_serializer(self, *args, **kwargs):
        return ImageSerializer(*args, **kwargs)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image = serializer.save()
        AWS_service.upload_file(image.name)
        # moderate_image(image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def get(self, request):
        print("hello")
        return Response(None,status=status.HTTP_201_CREATED)