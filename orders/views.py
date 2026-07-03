from django.shortcuts import render
from .models import Order

def place_order(request):
    # checkout handles order creation; this view can be a redirect or info page
    return render(request, 'orders/order_success.html')

def order_success(request):
    return render(request, 'orders/order_success.html')

def admin_current_orders(request):
    orders = Order.objects.filter(status='current').order_by('-placed_at')
    return render(request, 'orders/admin_current_orders.html', {'orders': orders})

def admin_order_history(request):
    orders = Order.objects.filter(status='archived').order_by('-placed_at')
    return render(request, 'orders/admin_order_history.html', {'orders': orders})
