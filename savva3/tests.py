from django.test import TestCase
from .helpers import savva
from .models import Setting

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
