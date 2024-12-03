from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, UserLoginForm, UserUpdateForm
from orders.models import Order

User = get_user_model()  # Используем кастомную модель пользователя

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Входим в систему после регистрации
            return redirect('base:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('base:index')
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:profile')  # Перенаправление на профиль после сохранения
    else:
        form = UserUpdateForm(instance=request.user)

    # Получение заказов текущего пользователя
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'account/profile.html', {'form': form, 'orders': orders})
def logout_view(request):
    logout(request)
    return redirect('base:index')


