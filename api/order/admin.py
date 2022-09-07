from django.contrib import admin
from .models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'user',
                    'product_id', 'total_products', 'total_amount']
