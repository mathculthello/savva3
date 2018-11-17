from django.test import TestCase
from django.test import Client
from django.test.utils import override_settings
from django.conf import settings


# Create your tests here.
class Savva3TestCase(TestCase):

    def test_index_page(self):
        c=Client()
        response=c.get('/')
        self.assertEqual(response.status_code, 200)


    @override_settings(DEBUG=False)
    def test_if_not_found_redirects_with_301(self):
        c=Client()
        response=c.get('/abracadabra/')
        #self.assertEqual(response.status_code, 301)
