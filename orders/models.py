from django.db import models
from catalog.models import Product

class Order(models.Model):
    PAYMENT_METHODS = [('COD', 'Cash on Delivery')]
    STATUS_CHOICES = [('current', 'Current'), ('archived', 'Archived')]

    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    postal_code = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, default='COD')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='current')
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def line_total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.quantity} × {self.product.title}"
