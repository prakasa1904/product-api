from django.contrib.auth.models import User, Group
from .models import Size, Color, Category, Product
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SizeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Size
		fields = ['name']

class ColorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Color
		field = ['name']

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['name']

'''
Data Hierarchy, sumber : http://voorloopnul.com/blog/representing-hierarchical-data-with-django-rest-framework/
Modify : Prakasa <prakasa@devetek.com>
'''
class RecursiveSerializer(serializers.Serializer):
	def to_representation(self, value):
		serializer = self.parent.parent.__class__(value, context=self.context)
		return serializer.data

class CategoryViewSerializer(serializers.ModelSerializer):
	subcategory_set = RecursiveSerializer(many=True, read_only=True)
	
	class Meta:
		model = Category
		fields = ('id', 'name', 'parent', 'subcategory_set')
'''
END:: From tutorial
'''

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	size = SizeSerializer(many=True, read_only=True)
	color = ColorSerializer(many=True, read_only=True)
	category = CategorySerializer(many=True, read_only=True)
	name = serializers.CharField()

	class Meta:
		model = Product
		fields = ('url', 'name', 'size', 'color', 'price', 'category')
