from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from catalog.models import Product
from account.models import User

@login_required
def create_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        comment = request.POST.get('comment')

        # Обновляем номер телефона, если он был изменен
        if phone_number and phone_number != request.user.phone_number:
            request.user.phone_number = phone_number
            request.user.save()

        # Создаем заказ
        order = Order.objects.create(
            user=request.user,
            product=product,
            address=address,
            comment=comment
        )

        return redirect('orders:order_success')  # Перенаправляем на страницу подтверждения или успеха

    return render(request, 'orders/create_orders.html', {'product': product, 'user': request.user})

def order_success(request):
    return render(request, 'orders/order_success.html')