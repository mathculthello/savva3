from django.shortcuts import render
from events.models import Event
from questions.forms import QuestionForm
from features.forms import FormulaeForm
from features.models import Formulae
from jokes.models import Joke
from base.models import Url
from django.contrib.flatpages.models import FlatPage

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
    context = {
    'intro':intro,
    'video':video,
    'formulae': formulae,
    'question_form':question_form,
    'formulae_form':formulae_form,
    'joke':joke,
    }
    return render (request, 'index.html', context)
