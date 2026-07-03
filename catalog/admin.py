from .models import Brand, Category, Subcategory, Product, ProductImage 
from django.contrib import admin

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage 
    extra = 1 
@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin): 
    list_display = ('title', 'brand', 'category', 'price', 'stock_quantity', 'is_active') 
    list_filter = ('brand', 'category', 'subcategories', 'is_active') 
    search_fields = ('title', 'brand__name') 
    prepopulated_fields = {'slug': ('title',)} 
    filter_horizontal = ('subcategories',) 

