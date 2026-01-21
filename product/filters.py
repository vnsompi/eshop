"""for filtering products  """
"""and searching product word """
#***************************************************************

from django_filters import rest_framework as filters
from .models import Product

#****************************************************************



class ProductFilter(filters.FilterSet):

    keywords = filters.CharFilter(field_name='keywords', lookup_expr='icontains')
    # this helps us to search words *********************************************
    min_price = filters.NumberFilter(field_name='price' or 0, lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price' or 1000000, lookup_expr='lte')
    #this line of code  helps me to the numeric value

    class Meta:

        model = Product
        fields = ('keywords','category','brand', 'min_price', 'max_price')
