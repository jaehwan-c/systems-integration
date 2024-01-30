from .models import Category, Brand

def categories(request):
    return {
        'categories': Category.objects.all()   
    }

def brands(request):
    return {
        'brands': Brand.objects.all()
    }