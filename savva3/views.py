from django.shortcuts import render, redirect
from events.models import Event
from features.models import Formulae
from jokes.models import Joke
from base.models import Url
from meta.views import Meta

from django.http import HttpResponseNotFound
from django.template import loader
from django.urls import reverse

from .menu import TOP_MENU, BOTTOM_MENU

ERROR_404_TEMPLATE_NAME = '404.html'


# Create your views here.
def index(request):
    joke=Joke.objects.filter(published=True).filter(adult=False).order_by('?').first()
    formulae=Formulae.objects.filter(published=True).order_by('?').first()
    video=Url.objects.filter(url__contains="youtube").filter(url__contains="watch").order_by("?").first()

    context = {
    'video':video,
    'formulae': formulae,
    'joke':joke,
    }
    return render (request, 'index.html', context)


# PAGES
def savvateev(request):
    return render(request,'pages/savvateev.html')

def savva_book(request):
    return render(request,'pages/savva_book.html')

def participate(request):
    return render(request,'pages/participate.html')

def team(request):
    return render(request,'pages/team.html')

def credits(request):
    return render(request,'pages/credits.html')

def sitemap(request):
    map=TOP_MENU+BOTTOM_MENU;
    return render(request,'pages/sitemap.html', {'map': map})

# HANDLERS
def handle404(request, exception):
    return redirect (reverse('404'), permanent=True)

def return404(request, template_name=ERROR_404_TEMPLATE_NAME):
    menu=TOP_MENU+BOTTOM_MENU;
    template = loader.get_template(template_name)
    context = {'menu': menu}
    body = template.render(context, request)
    content_type = None             # Django will use DEFAULT_CONTENT_TYPE
    return HttpResponseNotFound(body, content_type=content_type)
