from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Event



from .models import Event
# Create your views here.


def calendar(request):
    return render(request, 'events/calendar.html')


def details(request, event_id):
    event=Event.objects.get(id=event_id)
    return render(request, 'events/details.html', {'event':event})
