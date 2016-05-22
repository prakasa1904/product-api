"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from ver1 import views as apis
from frontend import views as frontend

router = routers.DefaultRouter()
router.register(r'users', apis.UserViewSet)
router.register(r'groups', apis.GroupViewSet)
router.register(r'category', apis.CategoryViewSet)
router.register(r'product', apis.ProductViewSet)

urlpatterns = [
	url(r'^$', frontend.index, name='index'),
	url(r'^admin/', admin.site.urls),
	url(r'^api/01/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
