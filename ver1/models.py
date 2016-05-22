from __future__ import unicode_literals

from django.db import models

class Size(models.Model):
	name = models.CharField(verbose_name='Size Name', max_length=2, unique=True, null=True, blank=True)

	class Meta:
		verbose_name = 'Size'

	def __unicode__(self):
		return u'%s' % (self.name)

class Color(models.Model):
        name = models.CharField(verbose_name='Color Name', max_length=250, unique=True, null=True, blank=True)
	
	class Meta:
		verbose_name = 'Color'
	
	def __unicode__(self):
		return u'%s' % (self.name)

class Category(models.Model):
	name  = models.CharField(verbose_name='Category Name', max_length=255, unique=True, default='Uncategorized')
	parent = models.ForeignKey('self', related_name='subcategory_set', null = True)

	class Meta:
		verbose_name = 'Category'

	def __unicode__(self):
		return u'%s' % (self.name)

class Product(models.Model):
	name = models.CharField(max_length=250, verbose_name='Product Name', null=False, blank=False)
	size = models.ManyToManyField(Size)
	color = models.ManyToManyField(Color)
	#size = models.CharField(max_length=1, verbose_name='Product Size')
	#color = models.CharField(max_length=250, verbose_name='Product Color', null=True)
	price = models.IntegerField(verbose_name='Product Price', null=False, blank=False,default=0)
	category = models.ManyToManyField(Category)

	class Meta:
		verbose_name = 'Product'

	def __str__(self):
		return self.name
