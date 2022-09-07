from django.db import models
import uuid


# Create your models here.
class Category(models.Model):
    category_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
