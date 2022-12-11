from django.shortcuts import render, redirect 
from .models import Prompt, Mood
from random import sample
import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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
            return redirect('welcom')
    return render(request, 'homeApp/login.html')

#This is the registration page
def regPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('welcom')
    return render(request, 'homeApp/reg.html')

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

# We also need a welcome page, to display the quote of the day as well as accept UI
# in the form of mood input from a sliding bar
def welcomePage(request):
    if request.method == 'POST':
        my_slider = request.POST['my_slider']
        todaysMood = my_slider
        today = datetime.date.today()
        mood = Mood(value=todaysMood, date=today)
        mood.save
        return redirect('homee')
    return render(request, 'homeApp/welcomePage.html')

#We also need a user settings page, where users can change their login info and 
#their notification settings


#We also need a previous entries page

#We will also want a mood tracker page to visually represent the moods that were input each day
def mood_graph(request):
    moods = Mood.objects.all()  # retrieve all mood records from the database
    dates = [mood.date for mood in moods]  # create a list of dates from the mood records
    values = [mood.value for mood in moods]  # create a list of values from the mood records
    context = {
        'dates': dates,
        'values': values,
    }
    return render(request, 'homeApp/mood_graph.html', context)

#Maybe a separate page for writing a new entry as well
def promptEntry(request, prompt_slug):
        selected_prompt = Prompt.objects.get(slug=prompt_slug)
        return render(request, 'homeApp/promptEntry.html',{
            'prompt_title': selected_prompt.title,
        })

#And a separate page for writing the daily entry
def dailyPromptEntry(request):
        return render(request, 'homeApp/promptEntry.html',{
            'prompt_title': "Explain your photo from today",
        })