from django.contrib import admin
from .models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description',
                    'price', 'stock', 'is_active', 'image']
