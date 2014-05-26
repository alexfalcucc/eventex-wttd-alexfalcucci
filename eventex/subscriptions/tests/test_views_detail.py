# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class DetailTest(TestCase):
        def setUp(self):
            s = Subscription.objects.create(name='Alexsander Falcucci', cpf='12345678901',
                                            email='alex.falcucci@gmail.com', phone='35-99913899')
            self.resp = self.client.get('/inscricao/%d/' % s.pk)
        def test_get(self):
            #Get /inscricao/1/ retorna code 200.
            self.assertEqual(200, self.resp.status_code)
        def test_template(self):
            self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

        def text_context(self):
            #Instancia de inscricao
            subscription = self.resp.context['subscription']
            self.assertIsInstance(subscription, Subscription)
        def test_html(self):
            self.assertContains(self.resp, 'Alexsander Falcucci')

class DetailNotFound(TestCase):
        def test_not_found(self):
            response = self.client.get('/inscricao/0/')
            self.assertEqual(404, response.status_code)
        