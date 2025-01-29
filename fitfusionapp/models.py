from django.db import models
from django.contrib.auth.models import User


class bench(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='equipmemnt/')

    def __str__(self):
        return self.name

class contactdetail(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=170)
    website=models.URLField(max_length=200, blank=True, null=True)
    comment=models.TextField()

    def __str__(self):
        return self.name
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(bench, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def total(self):
        return self.product.price * self.quantity


class billinginfo(models.Model):
    deliver = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_quantity = models.PositiveIntegerField()
    Deliver_details = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f"Order #{self.id} - {self.status}"
    
class orderitem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(bench, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def total(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.product.name} ({self.quantity})"