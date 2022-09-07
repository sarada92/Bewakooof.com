from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
import uuid

# Create your models here.


class CustomUser(AbstractUser):
    user_uuid = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, default='Anonymous')
    email = models.EmailField(max_length=25, unique=True, null=False)
    phone = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=5, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # Using custom manager for create user & create super user
    objects = UserManager()

    # By default Django takes username to login, We are setting it as False
    username = None
    # Setting Email as the login field
    USERNAME_FIELD = 'email'
    # Apart from Email & Password, which are other fields are required to login
    REQUIRED_FIELDS = []
