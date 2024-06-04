from django.urls import path, include
from .import views
from .views import ListPaymentTypesGenerics,DetailedPaymentTypesGenerics,SpecialPaymentTypesGenerics

urlpatterns = [
    path('payment_type_list/', views.ListPaymentTypesGenerics.as_view(), name="lpg"),
    path('payment_type_details/<int:pk>', views.DetailedPaymentTypesGenerics.as_view(), name="dpg"),
    path('payment_type_special/<int:pk>', views.SpecialPaymentTypesGenerics.as_view(), name="spg")
]
