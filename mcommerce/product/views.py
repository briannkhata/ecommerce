from django.shortcuts import render

from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import APIView # for class based views


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listproducts(request):
    query = Product.objects.all()
    products = ProductSerializer(query, many=True)
    context = {
        "products": products.data
    }
    return Response(context)

@permission_classes([IsAuthenticated])
class ListProducts(APIView):
    def get(self, request):
        query = Product.objects.all()
        products = ProductSerializer(query, many=True)
        context = {
            "products": products.data
        }
        return Response(context)

@permission_classes([IsAuthenticated])
class ProductDetails(APIView):
    def get(self, request, pid):
        query = Product.objects.filter(product_id=pid)
        products = ProductSerializer(query, many=True)
        context = {
            "products": products.data
        }
        return Response(context)
