from django.test import TestCase
from django.test import Client
from django.test.utils import override_settings
from django.conf import settings
from django.urls import reverse
from .models import Event
from django.utils import timezone
from .forms import InviteForm
from .models import Invite
from pprint import pprint

# Create your tests here.
class EventsTestCase(TestCase):

    def setUp(self):
        self.date=timezone.now()
        a=Event()
        a.title='test'
        a.start = self.date
        a.city = "Moscow"
        a.save()
        self.c=Client()


    def test_where_and_when_method(self):
        obj=Event.objects.first()
        expect = "%s, %s" % (obj.city, obj.start.strftime('%d %B %Y %H:%M'))
        self.assertEqual(obj.where_and_when(),expect)

    def test_index(self):
	# Переадресация на вики
        r=self.c.get('/events/')
        self.assertEqual(r.status_code,302)

    def test_archive(self):
        r=self.c.get('/events/archive/')
        self.assertEqual(r.status_code,200)

    def test_event(self):
        obj = Event.objects.first()
        url = reverse('events:event',args=[obj.id])
        r=self.c.get(url)
        self.assertEqual(r.status_code,200)

    def test_model_form(self):
        invite = Invite.objects.first()
        form = InviteForm(instance=invite) 
        pprint(form)
        self.assertEqual(form.name, "Егор")
