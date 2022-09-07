from django.contrib import admin
from .models import Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'name',
                    'description', 'created_at', 'updated_at']
