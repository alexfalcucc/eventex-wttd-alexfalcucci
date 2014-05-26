from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

def test_form_has_fields(self):
            # Formulario com 4 campos.
            form = self.resp.context['form']
            self.assertItemsEqual(['name','email','cpf','phone'], form.fields)