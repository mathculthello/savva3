from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Event



from .models import Event
# Create your views here.


def index(request):
    events=Event.objects.all().order_by('start')
    context={'events':events}
    return render(request, 'events/index.html',context)


def calendar(request):
    return render(request, 'events/calendar.html')


def event(request, event_id):
    event=Event.objects.get(id=event_id)
    return render(request, 'events/event.html', {'event':event})
