from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Event



from .models import Event
# Create your views here.


def archive(request):
    events=Event.objects.all()
    context={'events':events}
    return render(request, 'events/archive.html', context)

def events(request):
    events=Event.future.all()
    context={'events':events}
    return render(request, 'events/events.html',context)

def event(request, event_id):
    event=Event.objects.get(id=event_id)
    context={
    'event':event,
    'meta':event.as_meta(),
    }
    return render(request, 'events/event.html', context)
