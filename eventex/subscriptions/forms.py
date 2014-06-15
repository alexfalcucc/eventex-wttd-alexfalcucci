# coding: utf-8

from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

from django.core.validators import EMPTY_VALUES

from eventex.subscriptions.models import Subscription

def CPFValidator(value):
        if not value.isdigit():
            raise ValidationError(_(u'CPF deve conter apenas numeros!!'))
        if len(value) != 11:
            raise ValidationError(_(u'CPF deve ter 11 números!'))

class PhoneWidget(forms.MultiWidget):
        def __init__(self, attrs=None):
            widgets = (
                    forms.TextInput(attrs=attrs),
                    forms.TextInput(attrs=attrs))
            super(PhoneWidget, self).__init__(widgets, attrs)

        def decompress(self, value):
            if not value: return [None, None]
            return value.split('-')

class PhoneField(forms.MultiValueField):
        widget = PhoneWidget
        def __init__(self, *args, **kwargs):
            fields = (forms.IntegerField(),
                      forms.IntegerField())
            super(PhoneField, self).__init__(fields, *args, **kwargs)

        def compress(self, data_list):
            if not data_list: return ''
            if data_list[0] in EMPTY_VALUES: 
                raise forms.ValidationError(_(u'DDD Inválido.'))
            if data_list[1] in EMPTY_VALUES: 
                raise forms.ValidationError(_(u'Número inválido.'))
            return '%s-%s' %tuple(data_list)
        


class SubscriptionForm(forms.ModelForm):
        phone = PhoneField(label=_('Telefone'), required=False)
        class Meta:
            model = Subscription
            exclude = ('paid',)

        def __init__(self, *args, **kwargs):
            super(SubscriptionForm, self).__init__(*args, **kwargs)

            self.fields['cpf'].validators.append(CPFValidator)

        def clean_name(self):
            # nomes capitalizados com tratamento: da, de, dos...
            '''
            name = self.cleaned_data['name']
            words = name.split()
            for index, word in enumerate(words): # words = map(lambda w: w.capitalize(), name.split())
                if len(words[index]) > 3: words[index] = word.capitalize()
            nome_capitalizado = ' '.join(words)
            return nome_capitalizado'''

            name = self.cleaned_data['name']
            words = name.split()
            special_names = 'de da dos' 
            p_specials = special_names.split()
            for index, word in enumerate(words):
                words[index] = word.capitalize()
                for i, p in enumerate(p_specials):
                    p_specials[i] = p.capitalize()
                    if words[index] == p_specials[i]: 
                        words[index] = word.lower()
            nome_capitalizado = ' '.join(words)
            return nome_capitalizado

        def clean(self):
            super(SubscriptionForm, self).clean()
            if not self.cleaned_data['email'] and \
                not self.cleaned_data['phone']:
                  raise ValidationError(_(u'Informe seu e-mail ou telefone'))

            return self.cleaned_data
                


        # usando forms.Form
        #name = forms.CharField(label=_('Nome'))
        #cpf = forms.CharField(label=_('CPF'), max_length=11)
        #email = forms.EmailField(label=_('Email'))
        #phone = forms.CharField(label=_('Telefone'))