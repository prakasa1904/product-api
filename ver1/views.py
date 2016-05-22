from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import *
from .serializers import UserSerializer, GroupSerializer, CategoryViewSerializer, ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from .filter import *
import django_filters
from rest_framework import filters

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategoryViewSerializer

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	filter_fields = ('name', 'category', 'size', 'color', 'price')
	filter_class = ProductFilter
