from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Create new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Display success message
            messages.success(request, f"Account created for {username}!")

            # Redirect to a login page or homepage after successful registration
            return redirect('login')  # You can change this to wherever you want

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    return render(request, 'login.html')

