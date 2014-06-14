# coding: utf-8
from django.test import TestCase
from eventex.core.models import Talk
from eventex.core.managers import PeriodManager

class TalkModelTest(TestCase):
		def setUp(self):
			self.talk = Talk.objects.create(
				title=u'Introdução ao Django',
				description=u'Descrição da palestra',
				start_time='10:00')

		def test_create(self):
			self.assertEquals(1, self.talk.pk)

		def test_unicode(self):
			self.assertEquals(u'Introdução ao Django', unicode(self.talk))

		def test_speakers(self):
			#Talk has many Speakers and vice-versa.
			self.talk.speakers.create(name='Alexsander Falcucci',
									  slug='alexsander-falcucci',
									  url='http:/alexsanderfalcucci.com/')
			self.assertEquals(1, self.talk.speakers.count())

		def test_period_manager(self):
			# Talk default manager must be instance of PeriodManager
			self.assertIsInstance(Talk.objects, PeriodManager)