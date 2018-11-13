from django.test import TestCase
from django.test import Client
from django.test.utils import override_settings
from django.conf import settings
from django.urls import reverse
from .models import Event
import datetime

# Create your tests here.
class EventsTestCase(TestCase):

    def setUp(self):
        a=Event()
        a.title='test'
        a.start = datetime.datetime.now()
        a.save()
        self.c=Client()

    def test_index(self):
        r=self.c.get('/events/')
        self.assertEqual(r.status_code,200)

    def test_event(self):
        obj = Event.objects.first()
        url = reverse('events:event',args=[obj.id])
        r=self.c.get(url)
        self.assertEqual(r.status_code,200)
