from django.shortcuts import render, redirect
from events.models import Event
from features.models import Formulae
from jokes.models import Joke
from base.models import Url
from django.contrib.flatpages.models import FlatPage
from meta.views import Meta

from django.http import HttpResponseNotFound
from django.template import loader
from django.urls import reverse

ERROR_404_TEMPLATE_NAME = '404.html'


# Create your views here.
def index(request):
    joke=Joke.objects.filter(published=True).filter(adult=False).order_by('?').first()
    formulae=Formulae.objects.filter(published=True).order_by('?').first()
    video=Url.objects.filter(url__contains="youtube").filter(url__contains="watch").order_by("?").first()
    try:
        intro = FlatPage.objects.get(url='/intro/')
    except:
        intro = False

    try:
        meta = ModelMeta.objects.get(slug='/intro/')
    except:
        meta = False


    meta = {
    'keywords': ['Савватеев', 'математика', 'обучающие видео', 'популярная математика', 'обучение', 'видео'],
    'description': 'Популярная математика от Савватеева. Проект, где любой человек может взять и изучить интересующую его математическую тему.'
    }

    context = {
    'intro':intro,
    'video':video,
    'formulae': formulae,
    'joke':joke,
    'meta':meta,
    }
    return render (request, 'index.html', context)


# PAGES
def savvateev(request):
    meta = {
    'keywords': ['Алексей Савватеев', 'математик', 'популяризатор науки'],
    'description': 'Алексей Савватеев — математик, доктор физико-математических наук, активный популяризатор математики среди детей и взрослых.'
    }
    return render(request,'pages/savvateev.html',{'meta':meta})

def savva_book(request):
    meta = {
    'keywords': ['книга', 'математика', 'гуманитарии', 'лекции'],
    'description': 'Книга Алексея Савватеева по математике, адресованная гуманитариям.'
    }
    return render(request,'pages/savva_book.html',{'meta':meta})

def participate(request):
    meta = {
    'keywords': ['участие', 'поддержка', 'реквизиты', 'пожертвование', 'просветительская деятельность'],
    'description': 'Способы поучаствовать в проекте лектория Алексея Савватеева.'
    }
    return render(request,'pages/participate.html',{'meta':meta})

def team(request):
    meta = {
    'keywords': ['команда сайта'],
    'description': 'Люди, которые делают сайт savvateev.xyz'
    }
    return render(request,'pages/team.html',{'meta':meta})

def credits(request):
    meta = {
    'keywords': ['благодарности', 'список помощников'],
    'description': 'Люди, компании и явления, помогающие при работе над сайтом savvateev.xyz'
    }
    return render(request,'pages/credits.html',{'meta':meta})

def sitemap(request):
    meta = {
    'keywords': ['карта сайта', 'навигация', 'ссылки', 'разделы'],
    'description': 'Карта сайта Лектория Савватеева.'
    }
    return render(request,'sitemap.html',{'meta':meta})



# HANDLERS
def handle404(request, exception):
    return redirect (reverse('404'), permanent=True)

def return404(request, template_name=ERROR_404_TEMPLATE_NAME):
    template = loader.get_template(template_name)
    context = {}
    body = template.render(context, request)
    content_type = None             # Django will use DEFAULT_CONTENT_TYPE
    return HttpResponseNotFound(body, content_type=content_type)
