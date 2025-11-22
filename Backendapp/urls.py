from django.contrib import admin
from django.urls import path
from . import views 
from django.shortcuts import redirect


urlpatterns = [
    path('contact/', views.contact,  name='contact'),  
    path('', views.home, name='home'),  
    path('database/', views.database, name='database'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    
    
]