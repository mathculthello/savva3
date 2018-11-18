from django.db import models

from savva3.models import MetaClass

# Create your models here.

class Joke(MetaClass, models.Model):
    title = models.CharField(max_length=100,verbose_name="Название")
    author =  models.CharField(max_length=100, blank=False, default="", verbose_name="Кто добавляет")
    text = models.TextField(verbose_name="Содержание")

    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    published = models.BooleanField(default=False)
    already_in_book = models.BooleanField(default=False, verbose_name="Уже в книге")

    adult = models.BooleanField(default=False)


    def __str__(self):
        return self.title
