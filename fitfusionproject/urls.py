"""
URL configuration for fitfusionproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include , path
from fitfusionapp import views

urlpatterns = [
    path('',include('fitfusionapp.urls')),
    path('index/aboutus/',views.aboutus, name='aboutus'),
    path('index/aboutus/signin/',views.signin,name='signin'),
    path('index/aboutus/signin/register/',views.register,name='register'),
    path('index/aboutus/signin/register/contact/',views.contact,name='contact'),
    path('index/aboutus/signin/register/contact/trainingkit/',views.trainingkit,name='trainingkit'),
    path('index/aboutus/signin/register/contact/trainingkit/overproduct/',views.overproduct,name='overproduct'),
    path('index/aboutus/signin/register/contact/trainingkit/overproduct/summary/',views.summary,name='summary'),
    path('index/aboutus/signin/register/contact/trainingkit/overproduct/summary/foldablebench/',views.foldablebench,name='foldablebench'),
    path('index/aboutus/signin/register/contact/trainingkit/overproduct/summary/foldablebench/cartpage/',views.cartpage,name='cartpage'),
    path('index/aboutus/signin/register/contact/trainingkit/overproduct/summary/foldablebench/cartpage/address/',views.address,name='address'),
    path('index/aboutus/signin/register/contact/trainingkit/overproduct/summary/foldablebench/cartpage/address/user/',views.user,name='user'),
    path('index/aboutus/signin/register/contact/trainingkit/overproduct/summary/foldablebench/cartpage/address/user/yourorders/',views.yourorders,name='yourorders'),
    path('index/aboutus/signin/register/contact/trainingkit/overproduct/summary/foldablebench/cartpage/address/user/yourorders/dumbell/',views.dumbell,name='dumbell'),
      path('index/aboutus/signin/register/contact/trainingkit/overproduct/summary/foldablebench/cartpage/address/user/yourorders/dumbell/details/',views.details,name='details'),
    path('admin/', admin.site.urls),
]
