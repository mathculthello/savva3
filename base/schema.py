# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType

from .models import Url


class UrlType(DjangoObjectType):
    class Meta:
        model = Url

class Query(object):
    all_urls = graphene.List(UrlType)

    def resolve_all_urls(self, info, **kwargs):
        return Url.objects.all()
