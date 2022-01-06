from django.core import validators
import django_filters
from django_filters import NumberFilter, CharFilter
from .models import *
from django.core.validators import MinValueValidator

class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr='icontains', label="Product")
    category = CharFilter(field_name="category", lookup_expr='icontains', label="Category")
    brand = CharFilter(field_name="brand", lookup_expr='icontains', label="Brand")
    inventory_min = NumberFilter(field_name="countInStock", lookup_expr='gte', label="Min Inventory", validators=[MinValueValidator(0)])
    inventory_max = NumberFilter(field_name="countInStock", lookup_expr='lte', label="Max Inventory", validators=[MinValueValidator(0)])
    class Meta:
        model = Product
        fields = []
