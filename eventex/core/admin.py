from django.contrib import admin

# Register your models here.

from eventex.core.models import *

class Contactinline(admin.TabularInline):
		model = Contact
		extra = 1

class SpeakerAdmin(admin.ModelAdmin):
		inlines = [Contactinline,]
		prepopulated_fields = {'slug': ('name',)}



class Mediainline(admin.TabularInline):
		model = Media
		extra = 1

class TalkAdmin(admin.ModelAdmin):
		inlines = [Mediainline,]
		
		

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)