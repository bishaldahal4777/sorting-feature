from django.shortcuts import render
from .models import Product

def product(request):
    context = {'title': 'Home Page', 'username':'Bishal dahal'}
    return render(request, 'product/product.html', context)