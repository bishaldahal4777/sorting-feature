from django.shortcuts import render
from .models import Product
from django.http import JsonResponse, HttpResponse

def product(request):
    context = {'title': 'Home Page', 'username':'Bishal dahal', 'developer': 'Bishal Dev', 'skills':['python', 'git', 'sql']}
    return render(request, 'product/product.html', context)

def json_example(request):
    data = {'status':'success', 'Framework':'Django'}
    return JsonResponse(data)


def home(request):
    return HttpResponse("hey this is home page")

def form_view(request):
    name = None
    if request.method == 'POST':
        name = request.POST.get('username')
    return render(request, 'form.html', {'name':name})