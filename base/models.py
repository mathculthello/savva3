from django.db import models
from .utils import get_title
from django.core import exceptions
from django.urls import reverse
import datetime
from meta.models import ModelMeta







class Tag(models.Model):
    name = models.CharField(max_length=100, null=False)
    title = models.CharField(max_length=100, null=False, default='')
    def __str__(self):
        return self.title

class Area(models.Model):
    name = models.CharField(max_length=500, null=False)
    title = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title





class Person(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True


class Author(Person):
    pass





class Resource(ModelMeta, models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    areas = models.ManyToManyField(Area, blank=False)

    description = models.TextField(blank=True)

    comment = models.TextField(blank=True)

    authors = models.ManyToManyField(Author)

    created_at=models.DateTimeField(default=datetime.datetime.now, blank=False)
    updated_at=models.DateTimeField(default=datetime.datetime.now, blank=False)
    _keywords = models.CharField(max_length=500, blank=True)


    def __str__(self):
        return self.title

class Video(Resource):
    url = models.URLField(max_length=500, null=False, blank=False, unique=True)

    def get_absolute_url(self, *args):
        return reverse('base:video', kwargs={'video_id':self.id})




class Book(Resource):
    pass








# Create your models here.
class Url(ModelMeta, models.Model):
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=500, null=True)
    many_tag = models.ManyToManyField(Tag,blank=True, verbose_name='Тип', related_name="urls")
    areas = models.ManyToManyField(Area,blank=True, verbose_name='Раздел', related_name="urls")
    description = models.TextField(blank=True)

    status_code = models.IntegerField(null=True)

    updated_at=models.DateTimeField(default=datetime.datetime.now, blank=True)

    keywords_string = models.CharField(max_length=500, blank=True)

    _metadata = {
        'title': 'title',
        'description': 'description',
        'keywords': 'keywords'
    }

    def keywords(self):
        string=self.keywords_string
        if len(string)==0:
            return []
        return [x.strip() for x in string.split(",")]


    def save(self, *args, **kwargs):
        title=get_title(self.url)
        if(title):
            self.title=title
            super().save(*args, **kwargs)  # Call the "real" save() method.
        else:
            raise exceptions.ValidationError('hello')

    def get_absolute_url(self, *args):
        return reverse('base:details', kwargs={'url_id':self.id})


    def __str__(self):
        return self.title
