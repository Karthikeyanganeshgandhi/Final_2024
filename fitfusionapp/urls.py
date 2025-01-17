from django.urls import path
from fitfusionapp import views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('signin/',views.signin,name='signin'),
    path('register/',views.register,name='register'),
    path('contact/',views.contact,name='contact'),
    path('kit/',views.kit,name='kit'),
    path('overproduct/',views.overproduct,name='overproduct'),
    path('summary/',views.summary,name='summary'),
    path('foldablebench/',views.foldablebench,name='foldablebench'),
    path('cartpage/',views.cartpage,name='cartpage'),
    path('address/',views.address,name='address'),
    path('user/',views.user,name='user'),
    path('yourorders/',views.yourorders,name='yourorders'),
    path('dumbell/',views.dumbell,name='dumbell'),
    path('details/',views.details,name='details'),
]
