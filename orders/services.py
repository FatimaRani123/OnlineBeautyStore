from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .models import Order, OrderItem
from catalog.models import Product

def create_order_from_cart(cart, data):
    order = Order.objects.create(
        customer_name=data['customer_name'],
        email=data['email'],
        address=data['address'],
        postal_code=data['postal_code'],
        payment_method='COD',
        status='current',
    )
    # create items and decrement stock
    for item in cart.items.select_related('product'):
        product = item.product
        qty = item.quantity
        unit_price = product.price

        # stock validation
        if qty > product.stock_quantity:
            qty = product.stock_quantity  # clamp
        OrderItem.objects.create(order=order, product=product, quantity=qty, unit_price=unit_price)
        product.stock_quantity = max(0, product.stock_quantity - qty)
        product.save()

    # send confirmation email
    send_mail(
        subject='Beauty Store — Order Confirmation',
        message=_compose_confirmation_text(order),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[order.email],
        fail_silently=True,
    )
    return order

def _compose_confirmation_text(order):
    lines = [
        f"Hello {order.customer_name},",
        "Thank you for your order at Beauty Store!",
        "",
        "Order summary:",
    ]
    total = 0
    for oi in order.items.select_related('product'):
        line = f"- {oi.product.title} × {oi.quantity} @ PKR {oi.unit_price}"
        lines.append(line)
        total += oi.quantity * oi.unit_price
    lines += [
        "",
        f"Total: PKR {total}",
        "",
        "Delivery: Cash on Delivery",
        f"Address: {order.address}, {order.postal_code}",
        "",
        "We’ll reach out if anything changes.",
        "— Beauty Store"
    ]
    return "\n".join(lines)

def archive_old_orders():
    cutoff = timezone.now() - timedelta(days=2)
    Order.objects.filter(status='current', placed_at__lt=cutoff).update(status='archived')
