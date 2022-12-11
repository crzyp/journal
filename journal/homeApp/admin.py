from django.contrib import admin

from .models import Prompt
# Register your models here.

class PromptAdmin(admin.ModelAdmin):
	list_display= ('title',)
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Prompt, PromptAdmin)