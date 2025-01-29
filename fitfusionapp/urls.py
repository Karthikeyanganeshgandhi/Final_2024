from django.urls import path
from fitfusionapp import views

urlpatterns = [
    path('',views.index, name='index'),
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
    path('contacts/',views.contacts,name='contacts'),
    path('myaccount/',views.myaccount,name='myaccount'),
    path('main/',views.main,name='main'),
    path('reproduct/',views.reproduct,name='reproduct'),
    path('equipment/<int:product_id>/', views.prdetail, name='prdetail'),
    path('add/<int:product_id>/', views.add, name='add'),
    path('remove/<int:cart_item_id>/', views.remove, name='remove'),
    path('update/<int:cart_item_id>/', views.update, name='update'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-summary/<int:order_id>/', views.order_summary, name='order_summary'),
    path('placed//<int:order_id>/', views.placed, name='placed'),
    path('payment/<int:order_id>/', views.razorpay_payment, name='razorpay_payment'),   



]
