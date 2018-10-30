from django.test import TestCase
from django.db import models
from .models import Event, FutureManager
# Create your tests here.
class EventTestCase(TestCase):
    def setUp(self):
        pass

    def test_model_has_managers(self):
        """ Model has needed managers """
        self.assertEqual(Event.future, FutureManager())
        self.assertEqual(Event.objects, models.Manager())
