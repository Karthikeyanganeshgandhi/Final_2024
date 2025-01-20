from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import signform 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CartItem
from django.contrib.auth.decorators import login_required


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

from django.shortcuts import render,redirect,get_object_or_404
from .models import bench
def foldablebench(request):
    template=loader.get_template('Foldable_gymbench.html')
    return HttpResponse(template.render())


@login_required
def cartpage(request):
    cartitems = CartItem.objects.filter(user=request.user)
    total_quantity = sum(item.quantity for item in cartitems)
    total_price = sum(item.total() for item in cartitems)
    return render(request, 'cart_page.html', {'cartitems': cartitems, 'total_quantity': total_quantity, 'total_price': total_price})
@login_required
def add(request, product_id):
    product = get_object_or_404(bench, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product = product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cartpage')
@login_required
def remove(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cartpage')
@login_required
def update(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=request.user)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity.isdigit() and int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
    return redirect('cartpage')

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
    products = bench.objects.all()
    return render(request, 'class-details.html', {'products':products})

def prdetail(request, product_id):
    equipment = get_object_or_404(bench, pk=product_id)
    return render(request, 'renproduct.html' , {'equipment':equipment})

def myaccount(request):
    template=loader.get_template('myaccount.html')
    return HttpResponse(template.render())
def main(request):
    template=loader.get_template('myaccountmain.html')
    return HttpResponse(template.render())
def reproduct(request):
    template=loader.get_template('renproduct.html')
    return HttpResponse(template.render())