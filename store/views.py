from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import *

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def brands(request):
    return {
        'brands': Brand.objects.all()
    }

def product_all(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/products/single.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category_id=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})

def brand_list(request, category_slug):
    brand = get_object_or_404(Brand, slug=category_slug)
    products = Product.objects.filter(brand_id=brand)
    return render(request, 'store/products/category.html', {'brand': brand, 'products': products})