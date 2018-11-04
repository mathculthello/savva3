from django.shortcuts import render
from events.models import Event
from questions.forms import QuestionForm
from features.forms import FormulaeForm
from features.models import Formulae
from jokes.models import Joke
from base.models import Url
# Create your views here.
def index(request):
    joke=Joke.objects.order_by('?').first()
    question_form=QuestionForm()
    events = Event.future.order_by('start')
    formulae_form=FormulaeForm()
    formulae=Formulae.objects.filter(published=True).order_by('?').first()
    video=Url.objects.filter(url__contains="youtube").filter(url__contains="watch").order_by("?").first()
    context = {
    'video':video,
    'events': events,
    'formulae': formulae,
    'question_form':question_form,
    'formulae_form':formulae_form,
    'joke':joke,
    }
    return render (request, 'index.html', context)
