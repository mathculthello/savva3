from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<tag>', views.tag, name='tag')
]
