from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'unit_price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'email', 'status', 'placed_at')
    list_filter = ('status', 'placed_at')
    search_fields = ('customer_name', 'email')
    inlines = [OrderItemInline]
