from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.videos, name='videos'),
    path('<int:video_id>/', views.video, name='video'),
    path('books/', views.books, name="books"),
    path('book/<int:book_id>', views.book, name="book"),
]
