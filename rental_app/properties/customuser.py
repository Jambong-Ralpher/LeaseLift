from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='tenant')