from django.shortcuts import render, redirect 
from .forms import NewUserForm
from django.contrib import messages
from .models import Prompt
from random import sample
import datetime
from django.contrib.auth import login, authenticate

#This is the login page
def loginPage(request):
    if request.method == 'POST':
        # Get the username and password from the request.POST dictionary.
        username = request.POST['username']
        password = request.POST['password']

        # Use the authenticate() function to check if the user's credentials are valid.
        user = authenticate(request, username=username, password=password)

        # If the user's credentials are valid, log them in using the login() function.
        if user is not None:
            login(request, user)
            # Redirect the user to the home page.
            return redirect('homee')
    return render(request, 'homeApp/login.html')

#This is the registration page
def regPage(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('homee')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, 'homeApp/reg.html', context={"register_form":form})

#This is the Home page, which will display the prompts, the photos taken throught the day, 
# and the streaks
def home(request):
    #promptList = Prompt.objects.order_by('?')[:5]
    promptList = Prompt.objects.order_by('?').distinct()[:5]
    prompts = [
        {'title': promptList[0].title, 'slug': promptList[0].slug},
        {'title': promptList[1].title, 'slug': promptList[1].slug},
        {'title': promptList[2].title, 'slug': promptList[2].slug},
        {'title': promptList[3].title, 'slug': promptList[3].slug},
        {'title': promptList[4].title, 'slug': promptList[4].slug},
    ]
    return render(request, 'homeApp/home.html', {
        'prompts': prompts
    })

#We also need a user settings page, where users can change their login info and 
#their notification settings


#We also need a previous entries page
#already written in text_entry app