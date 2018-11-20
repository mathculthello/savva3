# cookbook/ingredients/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Event

class EventNode(DjangoObjectType):
    class Meta:
        model=Event
        filter_fields=['start']
        interfaces=(graphene.relay.Node, )

class Query(object):
    event = graphene.relay.Node.Field(EventNode)
    all_events = DjangoFilterConnectionField(EventNode)

    def resolve_all_events(self, info):
        return Event.future.all()
