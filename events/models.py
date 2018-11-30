from django.db import models
from django.urls import reverse
from django.utils import timezone
from meta.models import ModelMeta

from base.models import Video

from django.conf import settings

# First, define the Manager subclass.
class FutureManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(start__date__gte=timezone.now().date())

class Invite(models.Model):
	theme = models.CharField(max_length=200, blank=True, verbose_name="Предположительная тема")
	city = models.CharField(max_length=50, verbose_name="Город")
	name = models.CharField(max_length=40, verbose_name="Ваше имя")
	email = models.EmailField(max_length=200, verbose_name="Ваша электропочта")
	phone = models.CharField(max_length=30, verbose_name="Телефон")
	comment = models.TextField(blank=True, verbose_name="Пожелания")
	created_at = models.DateTimeField(auto_now_add=True)

class Event(ModelMeta, models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=300, blank=True)

    video = models.ManyToManyField(Video,blank=True)

    place = models.CharField(max_length=300, blank=True)

    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['start']


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
