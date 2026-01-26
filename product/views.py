"""this is when we are going to put all logic of product models"""

from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination

from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .filters import ProductFilter


"""this function is going to list all the product"""
@api_view(['GET'])
def get_products(request):

    #####################################################################"
    #"""for filtering products"""
    filterset = ProductFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    #"""used filter """
    #####################################################################"
    #add count
    count = filterset.qs.count()
    ####################################"""
     #add pagination
    resPerPage = 1
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage
    queryset = paginator.paginate_queryset(filterset.qs, request)
    #####################################################################"

    #products = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response({
        "count":count,
        "resPerPage":resPerPage,
        'products': serializer.data
    })

""" Single product """
@api_view(['GET'])
def get_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response({'product': serializer.data})