# jcJourney/models.py
from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_started = models.DateField()
    technologies_used = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20)
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name
