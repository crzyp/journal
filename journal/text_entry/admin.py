from django.contrib import admin

from .models import *
# Register your models here.

class EntryAdmin(admin.ModelAdmin):
	list_display= ('title', 'pub_date')
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Entry, EntryAdmin)