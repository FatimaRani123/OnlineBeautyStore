from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/<slug:brand_slug>/', views.brand_product_list, name='brand_product_list'),

    # New: products by category (includes subcategories)
    path('category/<slug:category_slug>/', views.category_products, name='category_products'),
    # New: products by subcategory
    path('subcategory/<slug:subcategory_slug>/', views.subcategory_products, name='subcategory_products'),

    # General product listing and details
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
