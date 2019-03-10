from django.contrib import admin
from .models import Sheet

# Класс для управления таблицей листков к 100 урокам в админ-панели
class SheetAdmin(admin.ModelAdmin):
    list_display = ['lesson_nums','lesson_name','sheet_url','author']

admin.site.register(Sheet, SheetAdmin) # Регистрируем классы в админ-панели