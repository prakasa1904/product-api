from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from .views import *

class ProductTestCase(TestCase):
	def setUp(self):
		pass
	
	def test_details(self):
		#url = reverse('product')
		#data = {'name': 'Demo'}
		#response = self.client.get(url, data, format='json')
		self.assertEqual(Product.objects.count(), 1)
