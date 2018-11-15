from django.db import models
from django.urls import reverse
from django.utils import timezone
from meta.models import ModelMeta

from base.models import Url

from django.conf import settings
import locale
# Create your models here.
locale.setlocale(locale.LC_TIME,settings.LANGUAGE_CODE)

# First, define the Manager subclass.
class FutureManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(start__date__gte=timezone.now().date())

class Event(ModelMeta, models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=300, blank=True)

    video = models.ManyToManyField(Url,blank=True)

    place = models.CharField(max_length=300, blank=True)

    comment = models.TextField(blank=True)

    pub_date = models.DateTimeField(auto_now_add=True, blank=True)


    #managers
    objects = models.Manager()
    future = FutureManager()

    _metadata = {
        'title': 'title',
        'description': 'where_and_when',
    }

    def url(self):
        return self.get_absolute_url(self)

    def where_and_when(self):
        return "%s, %s" % (self.city, self.start.strftime('%d %B %Y %H:%M'))

    def get_absolute_url(self, *args):
        return reverse('events:event', kwargs={'event_id':self.id})


    def __str__(self):
        return self.city
