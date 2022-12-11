from django.db import models
from django.utils.text import slugify

# individual entries to track 
# has a column for text
# has a column for an image
# has a column for the datetime
class Entry(models.Model):
	title = models.CharField(max_length=200)
	entry_text = models.TextField()
	image = models.ImageField(upload_to='uploads')
	pub_date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Entry, self).save(*args, **kwargs)
	
	def __str__(self):
		return f'{self.title} - {self.slug}'