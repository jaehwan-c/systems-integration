from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand', 'slug']
    prepopulated_fields = {'slug': ('brand',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'quantity', 'price', 'location']
    list_filter = ['category_id', 'location']
    list_editable = ['price', 'location', 'quantity']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass