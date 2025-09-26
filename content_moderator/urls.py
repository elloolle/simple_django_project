from django.urls import path
from rest_framework.routers import DefaultRouter

from .api.views import ImageModeratorView, ImageView, TextView, VideoView


router = DefaultRouter()
router.register("texts", TextView, basename="text")
router.register("images", ImageView, basename="image")
router.register("videos", VideoView, basename="video")
# router.register('moderate', ImageModeratorView.as_view(), basename='moderate/image')
urlpatterns = router.urls + [path(
    "moderate/", ImageModeratorView.as_view(), name="moderate"
)]
