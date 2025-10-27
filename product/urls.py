from django.urls import path
from django import views

urlpatterns = [
    path('product/', views.product, name= 'product')
]
