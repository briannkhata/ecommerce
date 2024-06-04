from django.shortcuts import render

from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import APIView  # for class based views


# Create your views here.
@authentication_classes([TokenAuthentication])
class ListCategories(APIView):
    def get(self, request):
        query = Category.objects.all()
        categories = CategorySerializer(query, many=True)
        context = {
            "categories": categories.data
        }
        return Response(context)

    def post(self, request):
        serializer_object = CategorySerializer(data=request.data)
        if serializer_object.is_valid(raise_exception=True):
            category_saved = serializer_object.save()
            return Response({"Success": "Category '{}' created successfully ".format(category_saved.category_name)})
        return Response(serializer_object.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([TokenAuthentication])
class CategoryDetails(APIView):
    def get(self, request, pid):
        query = Category.objects.filter(category_id=pid)
        categories = CategorySerializer(query, many=True)
        context = {
            "category": categories.data
        }
        return Response(context)

    def put(self, request, pid):
        category_obj = Category.objects.get(category_id=pid)
        serializer_obj = CategorySerializer(category_obj, data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            category_saved = serializer_obj.save()
            return Response({"Success": "Category '{}' updated successfully ".format(category_saved.category_name)})
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pid):
        Category.objects.filter(category_id=pid).delete()
        return Response(status=status.HTTP_200_OK)
