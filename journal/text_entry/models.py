from django.db import models

class Journal(models.Model):
	title_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Entry(models.Model):
	title = models.ForeignKey(Journal, on_delete=models.CASCADE)
	entry_text = models.TextField()
	image = models.ImageField(upload_to='/uploads/')

# Create your models here.
