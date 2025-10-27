# jcJourney/admin.py
from django.contrib import admin
from .models import LearningJourney, AboutMe

admin.site.register(LearningJourney)
admin.site.register(AboutMe)
