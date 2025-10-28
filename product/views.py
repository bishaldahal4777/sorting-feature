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
    return render(request, 'product/form.html', {'name':name})

def search_view(request):
    query = request.GET.get('q')
    return render(request, 'product/search.html',{'query': query})

def feedback_view(request):
    feedback_text = ''
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
    return render(request, 'product/feedback.html',{'feedback':feedback_text})

def contact_view(request):
    name=''
    message=''
    error=''
    if request.method=='POST':
        name = request.POST.get("name")
        message = request.POST.get("message")

        if not name or not message:
            print('fill out the form first')
    return render(request, 'product/contact.html', {'name': name, 'message':message, 'error':error})
