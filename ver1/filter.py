import django_filters
from .models import Product
from .serializers import SizeSerializer, ColorSerializer, CategorySerializer, ProductSerializer
from rest_framework import generics

class ProductFilter(django_filters.FilterSet):
	category = django_filters.CharFilter(name='category__name', lookup_type='contains')
	size = django_filters.CharFilter(name='size__name', lookup_type='contains')
	color = django_filters.CharFilter(name='color__name', lookup_type='contains')
	min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
	max_price = django_filters.NumberFilter(name="price", lookup_type='lte')
	
	class Meta:
		model = Product
		fields = ('name', 'size', 'color', 'price', 'category', 'min_price', 'max_price')
