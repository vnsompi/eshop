"""the serializers for our models product and models ProductImages  """

from .models import Product, ProductImage
from rest_framework import serializers


class ProductImageSerializer(serializers.ModelSerializer):
    """this is the serializer for the product model"""
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """this is the serializer for the product model"""
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price','brand','category','stock', 'images','user','images')
        ##############" Validations ##############"
        extra_kwargs = {
            "name": {"required": True, 'allow_blank': False},
            "description": {"required": True, 'allow_blank': False},
            "brand": {"required": True, 'allow_blank': False},
            "category": {"required": True, 'allow_blank': False},

        }
