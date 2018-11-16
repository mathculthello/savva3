from django.shortcuts import render
from .models import Video, Book

def videos(request):
    return render (request, 'base/videos.html')

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

def book(request, book_id):
    book = Book.objects.get(id=book_id)
    context={
    'book': book,
    'meta': book.as_meta()
    }
    return render(request, 'base/book.html', context)