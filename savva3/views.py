from django.shortcuts import render
from events.models import Event
from questions.forms import QuestionForm
# Create your views here.
def index(request):
    question_form=QuestionForm()
    events = Event.future.order_by('start')
    return render (request, 'index.html', {'events': events,'question_form':question_form})
