from django.db import models

# The journal column to track individual entries
# title refrences the entry and has a publishing date associated with it
class Journal(models.Model):
	title_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now_add=True)

# individual entries to track 
# title links it to the title in journal column
# has a column for text
# has a column for an image
class Entry(models.Model):
	title = models.ForeignKey(Journal, on_delete=models.CASCADE)
	entry_text = models.TextField()
	image = models.ImageField(upload_to='/uploads/')
