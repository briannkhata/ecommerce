from django.urls import path, include
from rest_framework.authtoken import views
from .views import ListCategories,CategoryDetails

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('category_list/', ListCategories.as_view(), name="category_list"),
    path('category_detail/<int:pid>/', CategoryDetails.as_view(), name="category_detail")
]
