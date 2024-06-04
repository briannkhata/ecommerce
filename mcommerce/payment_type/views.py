from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics, mixins

from .serializers import Payment_TypeSerializer
from .models import Payment_Type


# Create your views here.
class ListPaymentTypesGenerics(generics.ListAPIView,generics.CreateAPIView):
    queryset = Payment_Type.objects.all()
    serializer_class = Payment_TypeSerializer


class DetailedPaymentTypesGenerics(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Payment_Type.objects.all()
    serializer_class = Payment_TypeSerializer
    
 
 #special method   
class SpecialPaymentTypesGenerics(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment_Type.objects.all()
    serializer_class = Payment_TypeSerializer

