from django.db import models
from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer
from .customuser import CustomUser

# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='properties/')
    number_of_rooms = models.IntegerField()
    amenities = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    landlord = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    