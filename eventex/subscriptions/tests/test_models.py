# coding: utf-8
from django.test import TestCase
from datetime import datetime
from eventex.subscriptions.models import Subscription
from django.db import IntegrityError

class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Alexsander Falcucci',
			cpf='12345678901',
			email='alex.falcucci@gmail.com',
			phone='35-99914903'
		)

	def test_create(self):
		# inscricao contem name, cpf, email e phone.
		self.obj.save()
		self.assertEqual(1, self.obj.pk)

	def test_has_created_at(self):
		# inscricao must have automatic created_at
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_unicode(self):
			self.assertEqual(u'Alexsander Falcucci', unicode(self.obj))

	def teste_paid_default_value_is_False(self):
		#By default paid must be False.
		self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
		def setUp(self):
			# Criando primeiros atributos
			Subscription.objects.create(name='Alexsander Falcucci', cpf='12345678901', 
										email='alex.falcucci@gmail.com', phone='35-99913899')
		def test_cpf_unique(self):
			#CPF tem de ser UNICO
			s = Subscription(name='Alexsander Falcucci', cpf='12345678901', 
							email='email@dominio.com', phone='35-99913899')
			self.assertRaises(IntegrityError, s.save)

		def test_email_unique(self):
			#Email tem de ser UNICO
			s = Subscription(name='Alexsander Falcucci', cpf='00000000011', 
							email='alex.falcucci@gmail.com', phone='35-99913899')
			self.assertRaises(IntegrityError, s.save)

		

