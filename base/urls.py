from django.urls import path

from . import views

app_name = 'base'

urlpatterns = [
    path(r'', views.index, name='index'),
    path('<int:url_id>/', views.details, name='details'),
]
