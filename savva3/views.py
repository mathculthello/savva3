from django.shortcuts import render, redirect
from events.models import Event
from features.models import Formulae
from jokes.models import Joke
from base.models import Url, Video
from meta.views import Meta
from django.db import connection

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
def page(request, **kwargs):
    return render(request,kwargs['tpl'])

from finance.models import Transaction
from django.db.models import Sum
def participate(request):
    money = Transaction.objects.all()
    summary = money.aggregate(Sum('amount'))['amount__sum']
    context = {
    'transactions': money,
    'summary': summary
    }
    return render(request, 'pages/participate.html', context)

def sitemap(request):
    menus=TOP_MENU+BOTTOM_MENU;
    videos=Video.objects.all()
    events=Event.objects.all()
    context={
    'map':menus,
    'videos': videos,
    'events': events,
    }
    return render(request,'pages/sitemap.html', context)


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

# Sheets for 100 lessons.
def lessons_sheets(request):
    cursor = connection.cursor()
    cursor.execute("SELECT lesson_nums, lesson_name, sheet_url, author FROM sheets")
    ans = cursor.fetchall()
    context = {'table_sheets': ans}

    return render(request, 'pages/sheets.html', context)
