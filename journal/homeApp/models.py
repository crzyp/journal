from django.db import models

# Create your models here.

class Prompt(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

class Mood(models.Model):
    value = models.IntegerField()
    date = models.DateField()  # to use this format: YYYYMMDD, set the arguement to DATE_FORMAT='Ymd'