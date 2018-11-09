from django.urls import path

from . import views

app_name = 'base'

urlpatterns = [
    path('', views.app, name='index'),
    path('video/<str:video_id>', views.app, name="viewer"),
    path('<int:url_id>/', views.details, name='details'),
]
