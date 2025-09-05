from rest_framework.routers import DefaultRouter
from .views import RecipeView

router = DefaultRouter()
router.register('recipes', RecipeView, basename='recipe')
urlpatterns = router.urls