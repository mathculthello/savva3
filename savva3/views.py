from django.shortcuts import render, redirect
from events.models import Event
from questions.forms import QuestionForm
from features.forms import FormulaeForm
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
    question_form=QuestionForm()
    formulae_form=FormulaeForm()
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

    context = {
    'intro':intro,
    'video':video,
    'formulae': formulae,
    'question_form':question_form,
    'formulae_form':formulae_form,
    'joke':joke,
    }
    return render (request, 'index.html', context)

def sitemap(request):
    return render(request,'sitemap.html')

def handle404(request, exception):
    return redirect (reverse('404'), permanent=True)

def return404(request, template_name=ERROR_404_TEMPLATE_NAME):
    template = loader.get_template(template_name)
    context = {}
    body = template.render(context, request)
    content_type = None             # Django will use DEFAULT_CONTENT_TYPE
    return HttpResponseNotFound(body, content_type=content_type)
