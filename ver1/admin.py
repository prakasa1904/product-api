from django.contrib import admin

# Register Model To Admin
from .models import *

class SizeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class ColorAdmin(admin.ModelAdmin):
	list_display = ['name']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'parent')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Product)
