from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'), # ourwebsite.com/login
    path('register/', views.regPage, name='register'), # ourwebsite.com/register
    path('home/', views.home, name='homee'), # ourwebsite.com/home
]