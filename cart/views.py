from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from catalog.models import Product
from .models import CartItem
from .utils import get_cart
from orders.forms import CheckoutForm
from orders.services import create_order_from_cart

def cart_detail(request):
    cart = get_cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def add_to_cart(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id, is_active=True)
    # find existing item
    item = cart.items.filter(product=product).first()
    if item:
        if item.quantity + 1 > product.stock_quantity:
            messages.error(request, "Not enough stock available.")
        else:
            item.quantity += 1
            item.save()
            messages.success(request, "Added one more to cart.")
    else:
        if product.stock_quantity < 1:
            messages.error(request, "Product out of stock.")
        else:
            CartItem.objects.create(cart=cart, product=product, quantity=1)
            messages.success(request, "Product added to cart.")
    return redirect('cart:cart_detail')

def remove_from_cart(request, item_id):
    cart = get_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()
    messages.info(request, "Item removed from cart.")
    return redirect('cart:cart_detail')

def update_cart_item(request, item_id):
    cart = get_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    qty = int(request.POST.get('quantity', item.quantity))
    if qty < 1:
        item.delete()
        messages.info(request, "Item removed.")
    elif qty > item.product.stock_quantity:
        messages.error(request, "Not enough stock.")
    else:
        item.quantity = qty
        item.save()
        messages.success(request, "Quantity updated.")
    return redirect('cart:cart_detail')

def checkout(request):
    cart = get_cart(request)
    if cart.items.count() == 0:
        messages.error(request, "Your cart is empty.")
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = create_order_from_cart(cart, form.cleaned_data)
            # clear cart
            cart.items.all().delete()
            messages.success(request, "Order placed successfully.")
            return redirect('orders:order_success')
    else:
        form = CheckoutForm()
    return render(request, 'cart/checkout.html', {'cart': cart, 'form': form})
