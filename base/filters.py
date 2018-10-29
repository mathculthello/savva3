import django_filters
from django_filters import widgets
from .models import Url, Area, Tag
from django.db import models

class UrlFilter(django_filters.FilterSet):
    areas = django_filters.ModelChoiceFilter(
        queryset=Area.objects.all(),
        label="Разделы",
        widget=widgets.LinkWidget())
    many_tag = django_filters.ModelChoiceFilter(
        queryset=Tag.objects.all(),
        label="Тип",
        widget=widgets.LinkWidget())

    class Meta:
        model = Url
        fields = ['areas','many_tag',]
