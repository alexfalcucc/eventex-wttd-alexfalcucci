from django.contrib import admin

# Register your models here.

from eventex.core.models import Speaker, Contact

class Contactinline(admin.TabularInline):
		model = Contact
		extra = 1

class SpeakerAdmin(admin.ModelAdmin):
		inlines = [Contactinline,]
		prepopulated_fields = {'slug': ('name',)}

admin.site.register(Speaker, SpeakerAdmin)
