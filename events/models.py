from django.db import models
import datetime
from django.urls import reverse

from base.models import Url
# Create your models here.


# First, define the Manager subclass.
class FutureManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(start__date__gte=datetime.date.today())

class Event(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=300, blank=True)

    video = models.ManyToManyField(Url,blank=True)

    place = models.CharField(max_length=300, blank=True)

    comment = models.TextField(blank=True)

    pub_date = models.DateTimeField(default=datetime.datetime.now, blank=True)


    #managers
    objects = models.Manager()
    future = FutureManager()

    def url(self):
        return self.get_absolute_url(self)

    def get_absolute_url(self, *args):
        return reverse('events:event', kwargs={'event_id':self.id})


    def __str__(self):
        return self.city
