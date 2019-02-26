from django.urls import path
from savva3.utils import redirect_permanent

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events, name='events'),
    path('archive/', views.archive, name='archive'),
    path('invite/',redirect_permanent('invite'), name='invite'),
    path('<int:event_id>/', views.event, name='event'),
]
