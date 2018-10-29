from django.shortcuts import render
from calenda.models import Event
# Create your views here.
def index(request):
    events = Event.objects.order_by('start')
    return render (request, 'pages/index.html', {'events': events})

def page(request, page):
    template='pages/'+page+'.html'

    return render (request, template)
