from django.urls import path

from . import views

app_name = 'features'

urlpatterns = [
    path('formulae/add/', views.formulae_add, name='formulae_add')
]
