# ...existing code...
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import LearningJourney, AboutMe

def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'index.html', {'journeys': journeys})

def about_me(request):
    # return the first AboutMe instance (or None) and all users for the template
    about = AboutMe.objects.first()
    users = User.objects.all()
    return render(request, 'aboutMe.html', {'about': about, 'users': users})
# ...existing code...