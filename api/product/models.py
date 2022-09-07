from django.db import models
from api.category.models import Category
from api.user.models import CustomUser


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    merchant = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
