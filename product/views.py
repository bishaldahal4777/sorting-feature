from django.shortcuts import render
from .models import Product

def product(request):
    context = {'title': 'Home Page', 'username':'Bishal dahal', 'developer': 'Bishal Dev', 'skills':['python', 'git', 'sql']}
    return render(request, 'product/product.html', context)