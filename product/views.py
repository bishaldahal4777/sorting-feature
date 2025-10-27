from django.shortcuts import render
from .models import Product

def product_list(request):
    sort_by = request.GET.get("sort","name")
    Product.objects.all().order_by(sort_by)
    return render(request, 'product/product_list.html', {'sort_by': sort_by})

def product(request):
    return render(request, 'product/product.html')