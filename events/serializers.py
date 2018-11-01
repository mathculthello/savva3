from .models import Event
from rest_framework import serializers, permissions


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('title','start')
