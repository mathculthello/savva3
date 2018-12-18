from django.urls import path

from . import views

app_name = 'rating'

urlpatterns = [
    path('', views.update, name='update'),
]
