"""the serializers for our models product and models ProductImages  """

from .models import Product, ProductImage
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """this is the serializer for the product model"""
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    """this is the serializer for the product model"""
    class Meta:
        model = ProductImage
        fields = '__all__'