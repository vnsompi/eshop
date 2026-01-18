"""the serializers for our models product """

from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """this is the serializer for the product model"""
    class Meta:
        model = Product
        fields = '__all__'