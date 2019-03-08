
from django.db import models
from meta.models import ModelMeta
from django.utils import timezone as tz
from django.contrib import admin



class MetaClass(ModelMeta, models.Model):
    ''' Класс, содержащий дополнительную информацию для поисковиков '''
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    updated_at=models.DateTimeField(auto_now=True, blank=False)
    keywords = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)

    def date_field(self):
        return self.updated_at
        
    def get_keywords(self):
        return [x.strip() for x in self.keywords.split(',')]


    def get_description(self):
        return self.description


    class Meta:
        abstract=True

    _metadata = {
        'description': 'get_description',
        'keywords': 'get_keywords'
    }

# Класс для управления таблицей листков к 100 урокам в админ-панели
class SheetAdmin(admin.ModelAdmin):
    list_display = ['lesson_nums','lesson_name','sheet_url','author']

# Класс, отвечающий за листки к 100 урокам
class Sheets(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name = 'ID записи')
    subcategory_id = models.IntegerField(verbose_name = 'ID подкатегории')
    lesson_nums = models.TextField(blank=True, verbose_name = 'Номер урока')
    lesson_name = models.TextField(blank=True, verbose_name = 'Название урока')
    sheet_url = models.TextField(blank=True, verbose_name = 'Ссылка на листок')
    author = models.TextField(blank=True, verbose_name = 'Автор листка')
    objects = models.Manager()
    class Meta:
        managed = True
        db_table = 'sheets'         # Название таблицы в БД
        verbose_name = 'Листки'     # Отображаемое имя

admin.site.register(Sheets, SheetAdmin) # Регистрируем классы в админ-панели