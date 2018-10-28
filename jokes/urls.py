from django.urls import path

from . import views

app_name = 'jokes'

urlpatterns = [
    path('', views.index, name='index'),
    path('18/', views.yo, name='18'),
    path('add/', views.add, name='add')
]
