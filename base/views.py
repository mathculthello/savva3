from django.shortcuts import render, redirect
from .models import Resource, Progress, Video, Book

def videos(request):
    return render (request, 'base/videos.html')

def video(request,video_id):
    video = Video.objects.get(id=video_id)
    user=request.user
    try:
        progress = Progress.objects.get(resource=video, user=user)
    except:
        progress = False

    context={
    'viewed': progress,
    'video':video,
    'meta':video.as_meta()
    }
    return render (request, 'base/video.html',context)

def books(request):
    books = Book.objects.all()
    context={'books':books}
    return render (request, 'base/books.html', context)

def book(request, book_id):
    book = Book.objects.get(id=book_id)
    context={
    'book': book,
    'meta': book.as_meta()
    }
    return render(request, 'base/book.html', context)

def update_progress(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    user = request.user
    try:
        progress=Progress.objects.get(resource=resource, user=user)
        progress.delete()
    except:
        progress=Progress()
        progress.user=user
        progress.resource=resource
        progress.save()
    return redirect(request.META.get('HTTP_REFERER'))
