from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    tags=Tag.objects.all()
    urls=Url.objects.filter(many_tag=tags.first()).order_by('tag')
    context = {'tags': tags, 'urls': urls}
    return render (request, 'base/index.html',context)

def tag(request,tag):
    tags=Tag.objects.all()
    a=Tag.objects.get(name=tag)
    urls=Url.objects.filter(many_tag=a)
    context = {'tags': tags, 'tag': tag, 'urls': urls}
    return render (request, 'base/index.html',context)
