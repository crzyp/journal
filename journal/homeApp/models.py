from django.db import models

# Create your models here.

class Prompt(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)