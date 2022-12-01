from django.urls import path

import views

urlpatterns = [
	path('entry/', views.entry)
]