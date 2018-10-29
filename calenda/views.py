from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .serializers import EventSerializer

from rest_framework import viewsets, permissions
from .models import Event

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


from .models import Event
# Create your views here.
def index(request):
    return render(request, 'calenda/index.html')
