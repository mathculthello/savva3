from django.shortcuts import redirect, render
from .models import *

#from .filters import UrlFilter
from .models import Url

# Create your views here.
def app(request, **args):
    #f = UrlFilter(request.GET)
    #context = {'filter': f}
    return render (request, 'base/index.html')

def details(request,url_id):
    url = Url.objects.get(id=url_id)
    if 'youtube' in url.url:
        context={'url':url}
        return render (request, 'base/details.html',context)
    else:
        return redirect(url.url)
