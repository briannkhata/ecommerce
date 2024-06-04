
from django.urls import path, include
from .views import listproducts, ListProducts,ProductDetails

urlpatterns = [
    path('product_list/', listproducts, name="product_list"),
    path('product_list2/', ListProducts.as_view(), name="product_list2"),
    path('product_detail/<int:pid>/', ProductDetails.as_view(), name="product_detail")
]
