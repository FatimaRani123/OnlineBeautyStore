from django.shortcuts import render
from catalog.models import Category, Brand

def home(request):
    categories = Category.objects.prefetch_related('subcategories').order_by('name')
    brands = Brand.objects.all().order_by('name')[:10]
    return render(request, 'core/home.html', {'categories': categories, 'brands': brands})
