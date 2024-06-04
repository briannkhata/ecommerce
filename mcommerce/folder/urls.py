from django.urls import path, include
from .import views
from .views import get_all_folders

from rest_framework.routers import DefaultRouter,SimpleRouter

router = DefaultRouter()
router.register(
    'get_all_folders', get_all_folders, basename='folder'
)

# router = SimpleRouter()
# router.register(
#     'productviewset', FolderViewSet, basename='folder'
# )


urlpatterns = [] + router.urls
