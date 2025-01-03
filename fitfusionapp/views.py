from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def aboutus(request):
    template=loader.get_template('about-us.html')
    return HttpResponse(template.render())

def signin(request):
    template=loader.get_template('signin.html')
    return HttpResponse(template.render())

def register(request):
    template=loader.get_template('register.html')
    return HttpResponse(template.render())

def contact(request):
    template=loader.get_template('contact.html')
    return HttpResponse(template.render())
def trainingkit(request):
    template=loader.get_template('training_kit.html')
    return HttpResponse(template.render())
def overproduct(request):
    template=loader.get_template('overview_products.html')
    return HttpResponse(template.render())
def summary(request):
    template=loader.get_template('order_summary.html')
    return HttpResponse(template.render())
def foldablebench(request):
    template=loader.get_template('Foldable_gymbench.html')
    return HttpResponse(template.render())
def cartpage(request):
    template=loader.get_template('cart_page.html')
    return HttpResponse(template.render())
def address(request):
    template=loader.get_template('addresses.html')
    return HttpResponse(template.render())
def user(request):
    template=loader.get_template('services.html')
    return HttpResponse(template.render())
def yourorders(request):
    template=loader.get_template('your_orders.html')
    return HttpResponse(template.render())
def dumbell(request):
    template=loader.get_template('cast_iron_dumbell.html')
    return HttpResponse(template.render())
def details(request):
    template=loader.get_template('class-details.html')
    return HttpResponse(template.render())