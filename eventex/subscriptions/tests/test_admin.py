# cofing: utf-8
from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin

from mock import Mock

class MarkAsPaid(TestCase):
		def setUp(self):
			# Instancia o model Admin.
			self.model_admin = SubscriptionAdmin(Subscription, admin.site)

			# Popula o banco.
			Subscription.objects.create(name='Alexsander Falcucci', cpf='12345678901',
										email='alex.falcucci@gmail.com')

		def test_mark_all(self):
			#marcar todas como pago.
			fake_request = Mock()
			queryset = Subscription.objects.all()
			self.model_admin.mark_as_paid(fake_request, queryset)

			self.assertEqual(1, Subscription.objects.filter(paid=True).count())

		def test_has_action(self):
			'Action is installed'
			self.assertIn('mark_as_paid', self.model_admin.actions)
