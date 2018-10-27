from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    videos = AllMathVideo.objects.order_by('number')
    context = {'videos': videos}
    return render (request, 'allmath/index.html',context)
