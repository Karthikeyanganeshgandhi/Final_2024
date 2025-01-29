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

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Getting templates
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Getting templates
def aboutus(request):
    template=loader.get_template('about-us.html')
    return HttpResponse(template.render())

# --------------------------------------------------------------------------------------------------------------------------------------------------

# signin page function starts
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
# signin page function ends here

# ------------------------------------------------------------------------------------------------------------------------------------------------

# register page function starts here
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
# register page function ends here


# ------------------------------------------------------------------------------------------------------------------------------------------------
            
# contact page function starts here
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
# contact page function ends here

        
# ------------------------------------------------------------------------------------------------------------------------------------------------

def kit(request):
    template=loader.get_template('training_kit.html')
    return HttpResponse(template.render())

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Getting templates
def overproduct(request):
    template=loader.get_template('overview_products.html')
    return HttpResponse(template.render())

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Getting templates
def summary(request):
    template=loader.get_template('order_summary.html')
    return HttpResponse(template.render())


# -------------------------------------------------------------------------------------------------------------------------------------------------


from django.shortcuts import render,redirect,get_object_or_404
from .models import bench


# Getting templates
def foldablebench(request):
    template=loader.get_template('Foldable_gymbench.html')
    return HttpResponse(template.render())


# -------------------------------------------------------------------------------------------------------------------------------------------------

# Adding,removing,updating products into cart - function starting here

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

# Adding,removing,updating products into cart - function ends here

# -------------------------------------------------------------------------------------------------------------------------------------------

# Getting templates
def address(request):
    template=loader.get_template('addresses.html')
    return HttpResponse(template.render())

# -------------------------------------------------------------------------------------------------------------------------------------------

# Getting templates

@login_required
def user(request):
    return render(request, 'services.html', {'user': request.user})
# -------------------------------------------------------------------------------------------------------------------------------------------

# Getting templates
@login_required
def yourorders(request):
    orders = Order.objects.filter(user=request.user).order_by('order_date')

    return render(request, 'your_orders.html', {
        'orders': orders
    })

# -------------------------------------------------------------------------------------------------------------------------------------------

# Getting templates
def dumbell(request):
    template=loader.get_template('cast_iron_dumbell.html')
    return HttpResponse(template.render())

# -------------------------------------------------------------------------------------------------------------------------------------------

# Getting templates
def details(request):
    products = bench.objects.all()
    return render(request, 'class-details.html', {'products':products})

# -------------------------------------------------------------------------------------------------------------------------------------------

# Getting templates
def prdetail(request, product_id):
    equipment = get_object_or_404(bench, pk=product_id)
    return render(request, 'renproduct.html' , {'equipment':equipment})

# ------------------------------------------------------------------------------------------------------------------------------------------

# Getting templates
def myaccount(request):
    template=loader.get_template('myaccount.html')
    return HttpResponse(template.render())

# ------------------------------------------------------------------------------------------------------------------------------------------
# Getting templates
def main(request):
    template=loader.get_template('myaccountmain.html')
    return HttpResponse(template.render())

# -----------------------------------------------------------------------------------------------------------------------------------------
# Getting templates
def reproduct(request):
    template=loader.get_template('renproduct.html')
    return HttpResponse(template.render())

# ------------------------------------------------------------------------------------------------------------------------------------------
# Getting templates
def placed(request):
    template=loader.get_template('order_confirmation.html')
    return HttpResponse(template.render())


# ------------------------------------------------------------------------------------------------------------------------------------------

# fetching details form cartpage and display in order_confirmation page
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CartItem, billinginfo, Order, orderitem
from .forms import billingform

# Checkout View
@login_required
def checkout(request):
    # Fetch cart items for the logged-in user
    cart_items = CartItem.objects.filter(user=request.user)
    total_quantity = sum(item.quantity for item in cart_items)
    total_price = sum(item.total() for item in cart_items)

    # Redirect to cart if empty
    if total_quantity == 0:
        messages.warning(request, 'Your cart is empty!')
        return redirect('cartpage')

    # Retrieve or initialize billing info for the user
    billing_details = billinginfo.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = billingform(request.POST, instance=billing_details)
        if form.is_valid():
            # Save billing info with the logged-in user
            billing_details = form.save(commit=False)
            billing_details.user = request.user
            billing_details.save()
            
            cart_items = CartItem.objects.filter(user=request.user)
            total_price = sum(item.total() for item in cart_items)
            total_quantity = sum(item.quantity for item in cart_items)

            order = Order.objects.create(
                user=request.user,
                total_price=total_price,
                total_quantity=total_quantity,
                Deliver_details=billing_details.deliver,
            ) 

            for item in cart_items:
                orderitem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                )
            cart_items.delete()

            messages.success(request, 'Billing details updated and order placed successfully!')
            return redirect('order_summary', order_id=order.id)
    else:
        form = billingform(instance=billing_details)

    return render(request, 'order_summary.html', {
        'cart_items': cart_items,
        'total_quantity': total_quantity,
        'total_price': total_price,
        'form': form,
    })

# Order Summary View
@login_required
def order_summary(request, order_id):
    order = Order.objects.filter(id=order_id, user=request.user).first()
    if not order:
        messages.error(request, 'order not found.')
        return redirect('cartpage')
    
    order_items = orderitem.objects.filter(order=order)

    total_quantity = sum(item.quantity for item in order_items)
    total_price = sum(item.total() for item in order_items)


    order_items_with_names = [
        {
            'product_name': item.product.name,
            'quantity': item.quantity,
            'price': item.price,
            'total': item.quantity * item.price
        }
        for item in order_items
    ]

    return render(request, 'order_confirmation.html', {
        'order': order,
        'order_items': order_items_with_names,
        'total_quantity': total_quantity,
        'total_price': total_price,
    })

# ---------------------------------------------------------------------------------------------------------------------------------------------
# activating razorpay

import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Order  # Adjust the import based on your project structure

# Initialize Razorpay client
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@csrf_exempt
def razorpay_payment(request):
    if request.method == 'POST':
        try:
            # Get order details
            order_id = request.POST.get('order_id')
            order = Order.objects.get(id=order_id)
            total_price = order.total_price  # Ensure this field exists in your model

            # Razorpay amount should be in paise
            amount_in_paise = int(total_price * 100)

            # Create Razorpay order
            razorpay_order = client.order.create({
                "amount": amount_in_paise,
                "currency": "INR",
                "payment_capture": 1  # Auto-capture after payment
            })

            # Save Razorpay order ID to your database (optional)
            order.razorpay_order_id = razorpay_order['id']
            order.save()

            # Return Razorpay order details to the frontend
            return JsonResponse({
                'razorpay_order_id': razorpay_order['id'],
                'razorpay_key_id': settings.RAZORPAY_KEY_ID,
                'amount': amount_in_paise,
                'currency': "INR"
            })

        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=404)

    return JsonResponse({'error': 'Invalid Request'}, status=400)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------


