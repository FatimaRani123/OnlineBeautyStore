from django.shortcuts import render, get_object_or_404
from .models import Category, Subcategory, Brand, Product
from itertools import chain

def brand_list(request):
    brands = Brand.objects.all().order_by('name')
    return render(request, 'catalog/brand_list.html', {'brands': brands})

def brand_product_list(request, brand_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    products = Product.objects.filter(brand=brand, is_active=True).order_by('title')
    return render(request, 'catalog/product_list.html', {'products': products, 'context_title': f"Brand: {brand.name}"})

def product_list(request):
    products = Product.objects.filter(is_active=True).order_by('title')
    return render(request, 'catalog/product_list.html', {'products': products, 'context_title': 'All Products'})

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'catalog/product_detail.html', {'product': product})

# New: all products in a category (including subcategories)
def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products_direct = Product.objects.filter(category=category, is_active=True)
    products_sub = Product.objects.filter(subcategories__category=category, is_active=True)
    products = list({p.id: p for p in chain(products_direct, products_sub)}.values())
    products.sort(key=lambda p: p.title)
    return render(request, 'catalog/product_list.html', {'products': products, 'context_title': f"{category.name} products"})


# New: filter products by subcategory
def subcategory_products(request, subcategory_slug):
    sub = get_object_or_404(Subcategory, slug=subcategory_slug)
    products = Product.objects.filter(subcategories=sub, is_active=True).order_by('title')
    return render(request, 'catalog/product_list.html', {'products': products, 'context_title': f"{sub.category.name} — {sub.name}"})
