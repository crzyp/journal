from urllib.error import HTTPError
from django.shortcuts import render

# Create your views here.
def index(request):
	if request.method == "POST":
		
	return render(request, 'text_entry\index.html')