from django.db import models
from api.user.models import CustomUser
from api.product.models import Product
import uuid

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=False, null=True)
    total_products = models.IntegerField(default=0)
    transaction_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    total_amount = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
