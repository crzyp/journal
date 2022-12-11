from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'), # ourwebsite.com/login
    path('register/', views.regPage, name='register'), # ourwebsite.com/register
    path('home/', views.home, name='homee'), # ourwebsite.com/home
    path('welcome/', views.welcomePage, name='welcom'), # ourwebsite.com/welcome/
    path('home/mood-graph/', views.mood_graph), # ourwebsite.com/mood-graph/
    path('home/daily-photo-entry', views.dailyPromptEntry), #ourwebsite.com/home/<dynamic_path>
    path('home/<slug:prompt_slug>', views.promptEntry) #ourwebsite.com/home/<dynamic_path>
]