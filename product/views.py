"""this is when we are going to put all logic of product models"""

from django.shortcuts import get_object_or_404
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .filters import ProductFilter


"""this function is going to list all the product"""
@api_view(['GET'])
def get_products(request):

    #"""for filtering products"""
    filterset = ProductFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    #"""used filter """

    #products = Product.objects.all()
    serializer = ProductSerializer(filterset.qs, many=True)
    return Response({'products': serializer.data})

""" Single product """
@api_view(['GET'])
def get_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response({'product': serializer.data})