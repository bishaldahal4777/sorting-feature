from django.shortcuts import render, redirect
from .models import Product, Feedback, Practice
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.db.models import Q


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
        action = request.POST.get('action')

        if action == 'submit':
            name = request.POST.get("name")
            message = request.POST.get("message")

            if not name or not message:
                error='fill out the form first'
        elif action=='clear':
            name=''
            message=''
            error=''
    
        
    return render(request, 'product/contact.html', {'name': name, 'message':message, 'error':error})


def feedback_manager(request):
    error=''
    feedbacks = Feedback.objects.all().order_by('-created_at')

    if request.method=='POST':
        action = request.POST.get('action')

        if action == 'submit':
            name = request.POST.get('name')
            message=request.POST.get('message')

            if not name or not message:
                messages.error(request, "Please Fill out the form first")
            else:
                Feedback.objects.create(name=name, message=message)
                messages.success(request, "Successfully added new name and message")
                return redirect('feedback')

        elif action == 'clear':
            Feedback.objects.all().delete()
            messages.success(request, "succefully cleared all data")
            return redirect('feedback')


   
    return render(request, 'product/feedback_manager.html',{'error':error})

def practice_view(request):
    practices= Practice.objects.all().order_by('-created_at')

    if request.method == 'POST':
        name = request.POST.get('name','').strip()
        email = request.POST.get('email','').strip()
        message = request.POST.get('message', '').strip()

        has_error = False
        if not name:
            messages.error(request, 'Enter Name')
            has_error = True
        if not email:
            messages.error(request, 'Enter Email')
            has_error = True
        elif '@' not in email:
            messages.error(request, ' Email must have '@' ' )
            has_error = True 
        if not message:
            messages.error(request, 'Enter message')
            has_error = True
        elif len(message) < 10:
            messages.error(request,'message must be greater than 10')
            has_error = True
        
        if not has_error:
            Practice.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Form filled success')
            return redirect('practice')
    return render(request, 'product/practice.html', {'practices':practices})

def contact_list_view(request):
    query = request.GET.get('q', '').strip()
    practices = Practice.objects.all().order_by('-created_at')

    if query:
        practices = practices.filter(
            Q(name__icontains=query) | Q(email__icontains = query)
        )
        context = {'practices':practices,
                   'query':query}
    return render(request, 'product/practice_list.html', context)