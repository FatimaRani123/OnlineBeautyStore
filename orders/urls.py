from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('place/', views.place_order, name='place_order'),
    path('success/', views.order_success, name='order_success'),

    # Admin-facing simple pages (optional)
    path('admin/current/', views.admin_current_orders, name='admin_current_orders'),
    path('admin/history/', views.admin_order_history, name='admin_order_history'),
]
