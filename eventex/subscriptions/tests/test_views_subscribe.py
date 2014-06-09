# coding: utf-8
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

from django.core.urlresolvers import reverse as r

# Create your tests here.

class SubscribeTest(TestCase):
        def setUp(self):
            self.resp = self.client.get(r('subscriptions:subscribe'))

        def test_get(self):
            '''GET /inscricao/ retornará code 200.'''
            self.assertEqual(200, self.resp.status_code)

        def test_template(self):
            ''' response renderizando template'''
            self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

        def test_html(self):
            ''' Html contem inputs types '''
            self.assertContains(self.resp, '<form')
            self.assertContains(self.resp, '<input', 6)
            self.assertContains(self.resp, 'type="text"', 4)
            self.assertContains(self.resp, 'type="email"')
            self.assertContains(self.resp, 'type="submit"')
            
        def test_csrf(self):
            # form contem csrf token
            self.assertContains(self.resp, 'csrfmiddlewaretoken')
        def test_has_form(self):
            # Context must have the subscription form.
            form = self.resp.context['form']
            self.assertIsInstance(form, SubscriptionForm)

class SubscribePostTest(TestCase):
		def setUp(self):
			data = dict(name='Alexsander Falcucci', cpf="12345678901",
						email='alex.falcucci@gmail.com', phone='35-99913899')
			self.resp = self.client.post(r('subscriptions:subscribe'), data)
		def test_post(self):
			# Validando e redirecionando para /inscricao/1/

			self.assertEqual(302, self.resp.status_code)
		def test_save(self):
			#validando POST salvo
			self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
		def setUp(self):
			data = dict(name='Alexsander Falcucci', cpf="000000000012",
						email='alex.falcucci@gmail.com', phone='35-99913899')
			self.resp = self.client.post(r('subscriptions:subscribe'), data)
		def test_post(self):
			# Post invalido.
			self.assertEqual(200, self.resp.status_code)
		def test_form_erros(self):
			# formulario contem erros.
			self.assertTrue(self.resp.context['form'].errors)
		def test_dont_save(self):
			#Don't save data.
			self.assertFalse(Subscription.objects.exists())

class TemplateRegressionTest(TestCase):
		def test_template_has_non_field_errors(self):
			#'Check if non_field_errors are shown in template.'
			invalid_data = dict(name='Alexsander Falcucci', cpf='12345678901')
			response = self.client.post(r('subscriptions:subscribe'), invalid_data)
			self.assertContains(response, '<ul class="errorlist">')