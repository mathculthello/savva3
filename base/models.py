from django.db import models
from .utils import get_title
from django.core import exceptions


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


# Create your models here.
class Url(models.Model):
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=500, null=True)
    many_tag = models.ManyToManyField(Tag,blank=True, verbose_name='Тип', related_name="urls")
    areas = models.ManyToManyField(Area,blank=True, verbose_name='Раздел', related_name="urls")

    status_code = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        title=get_title(self.url)
        if(title):
            self.title=title
            super().save(*args, **kwargs)  # Call the "real" save() method.
        else:
            raise exceptions.ValidationError('hello')

    def __str__(self):
        return self.title
