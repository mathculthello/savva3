from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.calendar, name='calendar'),
    path('<int:event_id>/', views.details, name='details'),
]
