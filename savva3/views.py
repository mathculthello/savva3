from django.shortcuts import render
from events.models import Event
from questions.forms import QuestionForm
from features.forms import FormulaeForm
from features.models import Formulae
# Create your views here.
def index(request):
    question_form=QuestionForm()
    events = Event.future.order_by('start')
    formulae_form=FormulaeForm()
    formulae=Formulae.objects.order_by('?').first()
    context = {
    'events': events,
    'formulae': formulae,
    'question_form':question_form,
    'formulae_form':formulae_form,
    }
    return render (request, 'index.html', context)
