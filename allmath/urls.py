from django.urls import path

from . import views

app_name="allmath"

urlpatterns = [
    path('', views.index, name='index'),
]