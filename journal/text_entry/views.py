from django.shortcuts import render

from .models import Entry

# Create your views here.
def index(request):
	entries = Entry.objects.all()
	return render(request, 'text_entry\index.html', {
		'entries':entries
	})

def entry_details(request, entry_slug):
	try:
		selected_entry = Entry.objects.get(slug=entry_slug)
		return render(request, 'text_entry\entry_details.html', {
			'entry_found':True,
			'entry_image':selected_entry.image,
			'entry_title':selected_entry.title,
			'entry_date':selected_entry.pub_date,
			'entry_text':selected_entry.entry_text
		})
	except Exception as exc:
		return render(request, 'text_entry\entry_details.html', {
			'entry_found':False
		})