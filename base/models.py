from django.db import models
from .helpers import get_title
from django.core import exceptions
from django.urls import reverse
from meta.models import ModelMeta
from django.contrib.auth.models import User

from django.utils.translation import gettext as _
from embed_video.fields import EmbedVideoField

from savva3.models import MetaClass

### ABSTRACT CLASSES


class Rubricator(models.Model):
    ''' Класс, из которого можно делать рубрикаторы '''
    title = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        abstract=True
    def __str__(self):
        return self.title


class Person(models.Model):
    ''' Класс, представляющий людей '''
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True






### BASE CLASS

class Resource(MetaClass, models.Model):
    ''' Базовый класс, представляющий любой ресурс (видео, статья, книга, теорема...) '''
    title = models.CharField(max_length=500, null=False, blank=False)
    areas = models.ManyToManyField('Area', blank=False)
    description = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    authors = models.ManyToManyField('Author')
    relation = models.ManyToManyField('self', through='Relationship', symmetrical=False)
    def __str__(self):
        return self.title


### RELATION CLASS

class Relationship(models.Model):
    ''' Класс, задающий отношения между ресурсами '''
    # Виды отношений:
    RELATIONS = (
        ('depends', _('Depends on')),
        ('refers', _('Refers to')),
    )
    # Модель Resource ссылается сама на себя:
    from_resource = models.ForeignKey('Resource', related_name='from_resource', on_delete=models.DO_NOTHING)
    to_resource = models.ForeignKey('Resource', related_name='to_resource', on_delete=models.DO_NOTHING)
    type=models.CharField(max_length=20, choices=RELATIONS)


class Progress(models.Model):
    ''' Модель, которая хранит информацию о проработанных некоторым пользователем ресурсах '''
    user = models.ForeignKey(User, related_name='resource', on_delete=models.CASCADE)
    resource = models.ForeignKey('Resource', related_name='user', on_delete=models.DO_NOTHING)
    class Meta:
        # Не создавать повторяющиеся записи:
        unique_together = ('user', 'resource')


### CHILD CLASSES

class Tag(Rubricator):
    pass

class Area(Rubricator):
    pass

class Author(Person):
    pass

class Video(Resource):
    url = EmbedVideoField(max_length=500, null=False, blank=False, unique=True)
    def get_absolute_url(self, *args):
        return reverse('base:video', kwargs={'video_id':self.id})

    def get_description(self):
        if self.description:
            return self.description
        else:
            return "Видео в Лектории Савватеева: %s" % self.title

    _metadata = {
    'description': 'get_description',
    'keywords': 'get_keywords'
    }



class Book(Resource):
    md5 = models.CharField(max_length=300,blank=True)
    def get_absolute_url(self):
        return reverse('base:book', kwargs={'book_id':self.id})


class Theorem(Resource):
    text = models.TextField()





### DEPRECATED
### Этот класс до сих пор хранится, потому что в базе данных осталась информация, которая еще может пригодиться

# Create your models here.
class Url(ModelMeta, models.Model):
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=500, null=True)
    many_tag = models.ManyToManyField(Tag,blank=True, verbose_name='Тип', related_name="urls")
    areas = models.ManyToManyField(Area,blank=True, verbose_name='Раздел', related_name="urls")
    description = models.TextField(blank=True)

    status_code = models.IntegerField(null=True)

    updated_at=models.DateTimeField(auto_now=True, blank=True)

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

    #def get_absolute_url(self, *args):
    #    return reverse('base:details', kwargs={'url_id':self.id})


    def __str__(self):
        return self.title
