from django.test import TestCase
from .helpers import savva
from .models import Setting
from django.test import Client
from django.test.utils import override_settings
from django.conf import settings


# Create your tests here.
class SettingsTestCase(TestCase):
    def setUp(self):
        a=Setting()
        a.key='title';
        a.value='test';
        a.save()

    def test_if_settings_loaded(self):
        result = Setting.objects.all()
        settings={}
        for item in result:
            settings[item.key]=item.value
        self.assertEqual(settings['title'],'test')

    @override_settings(DEBUG=False)
    def test_if_not_found_redirects_with_301(self):
        c=Client()
        response=c.get('/abracadabra/')
        self.assertEqual(response.status_code, 301)
