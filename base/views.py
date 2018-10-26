from django.shortcuts import render
from .models import *

from .filters import UrlFilter

# Create your views here.
def index(request):
    f = UrlFilter(request.GET)
    context = {'filter': f}
    return render (request, 'base/index.html',context)
