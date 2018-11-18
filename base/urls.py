from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
	path('progress/<int:resource_id>/', views.update_progress, name="update_progress"),
    path('', views.videos, name='videos'),
    path('video/<int:video_id>/', views.video, name='video'),
    path('books/', views.books, name="books"),
    path('book/<int:book_id>', views.book, name="book"),
    path('courses/', views.courses, name="courses"),
]
