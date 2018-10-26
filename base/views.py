from django.shortcuts import render
from .models import Url

# Create your views here.
def index(request):
    urls=Url.objects.all()
    context = {'urls': urls}
    return render (request, 'base/index.html',context)
