from urllib.error import HTTPError
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'text_entry\entry.html')