from django.contrib import admin
from django.urls import path,include
from app import views 

urlpatterns = [
    
    path('', views.home),
    path('pages/home.html', views.home),
    path('pages/file-input.html', views.file),
    path('pages/dashboard.html', views.dashboard),
    path('pages/login.html', views.login),
    path('pages/signup.html', views.signup),
    path('pages/about.html', views.about),
    
    ]