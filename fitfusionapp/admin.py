from django.contrib import admin

# Register your models here.

from .models import bench, Order, orderitem
admin.site.register(bench)
admin.site.register(Order)
admin.site.register(orderitem)
