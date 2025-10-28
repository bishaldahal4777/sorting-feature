from django.shortcuts import render, redirect
from .models import Product, Feedback
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
                message.error(request, "Please Fill out the form first")
            else:
                Feedback.objects.create(name=name, message=message)
                message.success(request, "Successfully added new name and message")
                return redirect('feedback')

        elif action == 'clear':
            Feedback.objects.all().delete()
            message.success(request, "succefully cleared all data")
            return redirect('feedback')


    context={
        'error':error,
        'feedbacks':feedbacks
    }
    return render(request, 'product/feedback_manager.html',context)
