from django.shortcuts import render, redirect
from .models import Resource, Progress, Video, Book, Course

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

def courses(request):
    # Meta in template
    courses = Course.objects.all()
    context = {
    'courses': courses
    }
    return render(request, 'base/courses.html', context)

def update_progress(request, resource_id):
    ''' Функция отмечает факт проработки конкретного ресурса конкретным юзером '''
    resource = Resource.objects.get(id=resource_id)
    user = request.user
    try:
        # Если запись о просмотре существует, то удаляем
        progress=Progress.objects.get(resource=resource, user=user)
        progress.delete()
    except:
        # Если же не существует, то создаем запись
        progress=Progress()
        progress.user=user
        progress.resource=resource
        progress.save()
    # После всего возвращаем на предыдущую страницу
    return redirect(request.META.get('HTTP_REFERER'))
