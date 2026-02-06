"""this is when we are going to put all logic of product models"""

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import Product, ProductImage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductImageSerializer
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
################################
######### Single product##############
@api_view(['GET'])
def get_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response({'product': serializer.data})
###################################"

####################################
########Added a new Product#########
@api_view(['POST'])
def get_new_product(request):

    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        product = Product.objects.create(**data)
        res = ProductSerializer(product, many=False)
        return Response({'product': res.data})
    else:
        return Response(serializer.errors)

#####################################################
#####################################################

#################################################
#########" Upload ProductImages into AWS ###############
@api_view(['POST'])
def upload_product_images(request):
    data = request.data
    files = request.FILES.getlist('images')
### Associates uploaded images with a product.
##this code upload all images linked to each product in the database
    images = []
    for f in files:
       image = ProductImage.objects.create(product=Product(data['product']), image=f)
       images.append(image)
    serializer = ProductImageSerializer(images, many=True)

    return  Response(serializer.data)
####################################################
########## Update a product ####################
@api_view(['PUT'])
def update_product(request, pk):
    product = get_object_or_404(Product, id=pk)

    #-check if the user is same -todo
    product.name = request.data['name']
    product.description = request.data['description']
    product.price = request.data['price']
    product.category = request.data['category']
    product.brand = request.data['brand']
    product.ratings = request.data['ratings']
    product.stock = request.data['stock']

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response({'product': serializer.data})