from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm  # Assuming you have a custom registration form

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect URL
        else:
            return render(request, 'registration.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired redirect URL
            else:
                # Handle authentication failure with specific error messages
                error_message = "Invalid username or password."
                return render(request, 'login.html', {'form': form, 'error': error_message})
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')