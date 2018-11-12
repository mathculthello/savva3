from django.urls import path

from . import views

app_name = 'base'

urlpatterns = [
    path('', views.app, name='index'),
    path('<int:video_id>/', views.video, name='video'),
    path('books/', views.books, name="books"),
]
