from django.shortcuts import redirect, render
from .models import *

#from .filters import UrlFilter
from .models import Video

# Create your views here.
def app(request, **args):
    #f = UrlFilter(request.GET)
    #context = {'filter': f}
    return render (request, 'base/index.html')

def video(request,video_id):
    video = Video.objects.get(id=video_id)
    context={
    'video':video,
    'meta':video.as_meta()
    }
    return render (request, 'base/video.html',context)

def books(request):
    books = Book.objects.all()
    context={'books':books}
    return render (request, 'base/books.html', context)
