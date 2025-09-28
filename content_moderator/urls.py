from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .api.views import ImageModeratorView, ImageView, TextView, VideoView
from .api.views.Authentication import LogoutView, UserView, CustomLoginView

router = DefaultRouter()
router.register("texts", TextView, basename="text")
router.register("images", ImageView, basename="image")
router.register("videos", VideoView, basename="video")
router.register("moderate", ImageModeratorView, basename="moderate/image")
router.register("user", UserView, basename="user")

urlpatterns = router.urls + [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]
