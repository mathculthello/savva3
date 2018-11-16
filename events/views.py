from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Event



from .models import Event
# Create your views here.


def index(request):
    events=Event.objects.all().order_by('start')
    meta = {
    'keywords': ['расписание', 'открытые лекции', 'график', 'выступления', 'Савватеев'],
    'description': 'График открытых лекций Алексея Савватеева по математике',
    }
    context={'events':events, 'meta': meta}
    return render(request, 'events/index.html',context)

def event(request, event_id):
    event=Event.objects.get(id=event_id)
    context={
    'event':event,
    'meta':event.as_meta(),
    }
    return render(request, 'events/event.html', context)
