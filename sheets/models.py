from django.db import models
from meta.models import ModelMeta

class Categories(models.Model):
    ''' Категории уроков из PDF-схемы '''
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, verbose_name='Имя категории')

class Subcategories(models.Model):
    ''' Подкатегории уроков из PDF-схемы '''
    id = models.IntegerField(primary_key=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.TextField(blank=True, verbose_name='Имя подкатегории')

class Sheet(models.Model):
    ''' Модель, хранящая информацию по каждому уроку (из 100 уроков) '''
    id = models.IntegerField(primary_key=True, verbose_name='ID записи')
    subcategory_id = models.IntegerField(verbose_name='ID подкатегории')
    lesson_nums = models.TextField(blank=True, verbose_name='Номер урока')
    lesson_name = models.TextField(blank=True, verbose_name='Название урока')
    sheet_url = models.TextField(blank=True, verbose_name='Ссылка на листок')
    author = models.TextField(blank=True, verbose_name='Автор листка')
    objects = models.Manager()

    def __str__(self):
        return ("%s %s %s %s" % (self.lesson_nums, self.lesson_name, self.sheet_url, self.author))