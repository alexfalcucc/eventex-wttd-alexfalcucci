from django.test import TestCase

from django.core.urlresolvers import reverse as r

# Create your tests here.

class HomeTest(TestCase):
	def setUp(self):
		self.resp = self.client.get(r('core:home'))

	def test_get(self):
		'''
			GET / para return 200
		'''
		response = self.client.get('/')
		self.assertEqual(200, response.status_code)
		self.assertTemplateUsed(response, 'index.html')

	def test_template(self):
		'''
			template mais utilizado = index.html
		'''
		self.assertTemplateUsed(self.resp, 'index.html')
		
		