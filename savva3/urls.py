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
from . import views
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
### sitemap
from django.contrib.sitemaps.views import sitemap
from .sitemaps import sitemaps
from django.views.generic import TemplateView
#handler404 = 'savva3.views.handle404'
from django.urls import reverse_lazy


from django.views.generic import RedirectView





from django.contrib.staticfiles.urls import staticfiles_urlpatterns



def redirect_permanent(name):
    return RedirectView.as_view(url=reverse_lazy(name), permanent=True)



urlpatterns = [
    # First, redirects
    path('books/', redirect_permanent('base:books')),


    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', views.index, name='index'),
    path(r'graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('base/', include('base.urls')),

    path('jokes/', include('jokes.urls')),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('features/', include('features.urls')),
    path('404/', views.return404, name='404'),
    path('sitemap/', views.sitemap, name='sitemap'),


    # Static pages

    path('savvateev/', views.page, {'tpl': 'pages/savvateev.html'}, name='savvateev'),
    path('book/', views.page, {'tpl':'pages/savva_book.html'}, name='savva_book'),
    path('participate/', views.page, {'tpl': 'pages/participate.html'}, name='participate'),
    path('team/', views.page, {'tpl': 'pages/team.html'}, name='team'),
    path('credits/', views.page, {'tpl': 'pages/credits.html'}, name='credits'),

    #path('', include('django.contrib.flatpages.urls')),
]


if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()