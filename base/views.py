from django.shortcuts import render
from .models import *

from django_filters import FilterSet


class UrlFilter(FilterSet):
    class Meta:
        model = Url
        fields = {
            'many_tag': ['exact'],
            'areas': ['exact'],
            'tag': ['exact'],
            'title': ['contains']
        }


# Create your views here.
def index(request):
    f = UrlFilter(request.GET, queryset=Url.objects.all())
    context = {'filter': f}
    return render (request, 'base/index.html',context)

def tag(request,tag):
    tags=Tag.objects.all()
    a=Tag.objects.get(name=tag)
    urls=Url.objects.filter(many_tag=a)
    context = {'tags': tags, 'tag': tag, 'urls': urls}
    return render (request, 'base/index.html',context)
