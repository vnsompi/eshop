"""this is when we are going to put all logic of product models"""

from django.shortcuts import render
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer


"""this function is going to list all the product"""
@api_view(['GET'])
def get_products(request):

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response({'products': serializer.data})

