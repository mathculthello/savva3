from django_filters import FilterSet
from .models import Url

class UrlFilter(FilterSet):
    class Meta:
        model = Url
        fields = {
            'many_tag': ['exact'],
            'areas': ['exact'],
            'title': ['contains']
        }
