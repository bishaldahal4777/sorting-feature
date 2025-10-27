from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name= 'product'),
    path('json/', views.json_example, name= 'json')


]


