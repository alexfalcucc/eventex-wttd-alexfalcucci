from django.contrib import admin

from eventex.subscriptions.models import Subscription

from django.utils.timezone import now

from django.utils.translation import ugettext as _

# Register your models here.

class SubscriptionAdmin(admin.ModelAdmin):
			list_display = ('name','email','cpf','phone','created_at', 'subscribed_today','paid')
			date_hierarchy = 'created_at' # install pytz --> pip install pytz
			search_fields = ('nome','email','cpf','phone','created_at')
			list_filter = ['created_at']

			def subscribed_today(self, obj):
				return obj.created_at.date() == now().date()
			subscribed_today.short_description = _(u'Inscrito hoje?')
			subscribed_today.boolean = True
		
admin.site.register(Subscription, SubscriptionAdmin)
