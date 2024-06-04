from django.urls import path, include
from .import views
# from .views import ListCategories,CategoryDetails

urlpatterns = [
    path('mixinpath/', views.ListPlanMixins.as_view(), name="mp"),
    path('planmixin/<int:pk>/', views.DetailedPlanMixins.as_view(), name="mdp")
]
