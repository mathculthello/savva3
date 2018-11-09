from django.shortcuts import render
from .models import *

#from .filters import UrlFilter
from .models import Url

# Create your views here.
def index(request):
    #f = UrlFilter(request.GET)
    #context = {'filter': f}
    return render (request, 'base/index.html')

def details(request,id):
    url = Url.objects.get(id)
    return render (request, 'base/index.html',context)
