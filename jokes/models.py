from django.db import models

# Create your models here.

class Joke(models.Model):
    title = models.CharField(max_length=100,verbose_name="Название")
    author =  models.CharField(max_length=100, blank=True, verbose_name="Кто добавляет")
    text = models.TextField(verbose_name="Содержание")

    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
