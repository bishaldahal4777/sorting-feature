from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
def product(request):
    context = {'title': 'Home Page', 'username':'Bishal dahal', 'developer': 'Bishal Dev', 'skills':['python', 'git', 'sql']}
    return render(request, 'product/product.html', context)

def json_example(request):
    data = {'status':'success', 'Framework':'Django'}
    return JsonResponse(data)