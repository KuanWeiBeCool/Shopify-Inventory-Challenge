import django_filters
from django_filters import NumberFilter, CharFilter
from .models import *

class ProductFilter(django_filters.FilterSet):
    inventory_min = NumberFilter(field_name="countInStock", lookup_expr='gte', label="Min Inventory")
    inventory_max = NumberFilter(field_name="countInStock", lookup_expr='lte', label="Max Inventory")
    name = CharFilter(field_name="name", lookup_expr='icontains', label="Product")
    category = CharFilter(field_name="category", lookup_expr='icontains', label="Category")
    brand = CharFilter(field_name="brand", lookup_expr='icontains', label="Brand")
    class Meta:
        model = Product
        fields = ['name', 'category', 'brand', 'countInStock']
