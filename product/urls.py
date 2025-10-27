from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name= 'product'),
    path('json/', views.json_example, name= 'json'),
    path('home/', views.home, name= 'home'),
    path('form/', views.form_view, name= 'form'),



]


