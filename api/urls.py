from rest_framework.routers import DefaultRouter
from .views import TextView, ImageView, VideoView

router = DefaultRouter()
router.register('texts', TextView, basename='text')
router.register('images', ImageView, basename='image')
router.register('videos', VideoView, basename='video')
urlpatterns = router.urls