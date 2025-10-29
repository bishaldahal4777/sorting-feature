from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name= 'product'),
    path('json/', views.json_example, name= 'json'),
    path('home/', views.home, name= 'home'),
    path('form/', views.form_view, name= 'form'),
    path('search/', views.search_view, name= 'search'),

    path('contact/', views.contact_view, name= 'contact'),
    path('feedback/', views.feedback_manager, name= 'feedback'),
    path('practice/', views.practice_view, name= 'practice'),
    path('practice_list/', views.practice_list_view, name= 'practice_list'),









]


