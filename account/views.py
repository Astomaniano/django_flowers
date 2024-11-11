from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'account/profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')
