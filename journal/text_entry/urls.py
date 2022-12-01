from django.urls import path

import views

urlpatterns = [
	path('text_entry/', views.entry)
]