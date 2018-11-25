from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events, name='events'),
    path('archive/', views.archive, name='archive'),
    path('invite/',views.invite, name='invite'),
    path('<int:event_id>/', views.event, name='event'),
]
