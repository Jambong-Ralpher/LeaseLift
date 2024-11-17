from django.urls import path, include
from rest_framework.authtoken import views  # For token-based authentication
from . import views  # Import your views file for user registration and login
urlpatterns = [
    # ... other URL patterns for your application ...

    # Registration endpoint (assuming a view named 'register' in your views file)
    path('api/register/', views.register, name='register'),

    # Login endpoint (assuming a view named 'login' in your views file)
    path('api/login/', views.login, name='login'),

]