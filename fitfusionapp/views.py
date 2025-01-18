from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import signform 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def aboutus(request):
    template=loader.get_template('about-us.html')
    return HttpResponse(template.render())

def signin(request):
    if request.method == 'POST':
        form = signform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('details') 
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = signform()

    return render(request, 'signin.html', {'form': form})

from .forms import registerform  

def register(request):
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            passwd = form.cleaned_data['passwd']
            # phone_number = form.cleaned_data['phone_number']
            
            user = User.objects.create_user(username=email, email=email, password=passwd)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            messages.success(request, f'Account created for {first_name} {last_name}')
            return redirect('signin')
    else:
        form = registerform()
    return render(request, 'register.html', {'form':form})

            

from .models import contactdetail
from .forms import contactform

def contact(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
                form.save()
                return redirect('contacts')
        
    else:
        form=contactform()

    return render(request,'contact.html',{'form':form})

def contacts(request):
    det=contactdetail.objects.all()
    return render(request,'services.html',{'det':det})

            
        

def kit(request):
    template=loader.get_template('training_kit.html')
    return HttpResponse(template.render())
def overproduct(request):
    template=loader.get_template('overview_products.html')
    return HttpResponse(template.render())
def summary(request):
    template=loader.get_template('order_summary.html')
    return HttpResponse(template.render())

from .models import bench
def foldablebench(request):
   product = bench.objects.all()
   return render(request, 'class-details.html', {'product':product})

def productdetail(request, product_id):
    equipment = get_object_or_404(bench, id=product_id)
    return render(request, 'renderproduct.html' , {'equipment':equipment})


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
def myaccount(request):
    template=loader.get_template('myaccount.html')
    return HttpResponse(template.render())
def main(request):
    template=loader.get_template('myaccountmain.html')
    return HttpResponse(template.render())
def reproduct(request):
    template=loader.get_template('renderproduct.html')
    return HttpResponse(template.render())