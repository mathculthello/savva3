"""savva3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.views.decorators.csrf import csrf_exempt


from graphene_django.views import GraphQLView

### sitemap

from django.contrib.sitemaps.views import sitemap
from .sitemaps import sitemaps

### ROUTER REST
from rest_framework import routers
router = routers.DefaultRouter()

from events.rest.viewsets import EventViewSet
router.register(r'events', EventViewSet)


from django.views.generic import TemplateView
handler404 = 'savva3.views.handle404'


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', views.index, name='index'),
    path(r'graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path(r'api/', include(router.urls)),
    path('base/', include('base.urls')),
    path('jokes/', include('jokes.urls')),
    path('q/', include('questions.urls')),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('features/', include('features.urls')),
    path('404/', views.return404, name='404'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('', include('django.contrib.flatpages.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
