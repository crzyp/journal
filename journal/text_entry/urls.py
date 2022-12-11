from django.urls import path

from . import views

urlpatterns = [
	path('entry/', views.index, name='all-entries'),
	path('entry/new_entry', views.new_entry, name='new-entry'),
	path('entry/<slug:entry_slug>', views.entry_details, name='entry-detail'),
]