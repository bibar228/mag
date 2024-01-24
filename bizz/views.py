from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from bizz.models import Products
from bizz.serializers import ProductsSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductsSerializer