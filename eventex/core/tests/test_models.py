# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker, Contact
from django.core.exceptions import ValidationError

class SpeakerModelTest(TestCase):
		def setUp(self):
			self.speaker = Speaker(name='Alexsander Falcucci',
						   slug='alexsander-falcucci',
						   url='http://alexsanderfalcucci.com',
						   description='Passionate Software Developer!!!')
			self.speaker.save()

		def test_create(self):
			#Speaker instance should be saved.
			self.assertEqual(1, self.speaker.pk)

		def test_unicode(self):
			#Speaker string representation should be the name.
			self.assertEqual(u'Alexsander Falcucci', unicode(self.speaker))

class ContactModelTest(TestCase):
		def setUp(self):
			self.speaker = Speaker.objects.create(name='Alexsander Falcucci', 
												  slug='alexsander-falcucci',
												  url='http://alexsanderfalcucci.com',
												  description='Passionate Software Developer!!!')
		def test_email(self):
			contact = Contact.objects.create(speaker=self.speaker, kind='E',
											 value='alex.falcucci@gmail.com')
			self.assertEqual(1, contact.pk)

		def test_phone(self):
			contact = Contact.objects.create(speaker=self.speaker, kind='P',
											 value='21-996186180')
			self.assertEqual(1, contact.pk)

		def test_fax(self):
			contact = Contact.objects.create(speaker=self.speaker, kind='F',
											 value='21-12345678')
			self.assertEqual(1, contact.pk)
		
		def test_king(self):
			#Contact kind should be limited to E, P or F.
			contact = Contact(speaker=self.speaker, kind='A', value='B')
			self.assertRaises(ValidationError, contact.full_clean)

		def test_unicode(self):
			#Contact string representation should be Value
			contact = Contact(speaker=self.speaker, kind='E',
							  value='alex.falcucci@gmail.com')
			self.assertEqual(u'alex.falcucci@gmail.com', unicode(contact))
