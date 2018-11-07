# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType

from .models import Url


class UrlType(DjangoObjectType):
    class Meta:
        model = Url

class Query(object):
    all_urls = graphene.List(UrlType)
    random_url = graphene.Field(UrlType)

    def resolve_all_urls(self, info, **kwargs):
        return Url.objects.all()

    def resolve_random_url(serlf,info,**kwargs):
        return Url.objects.filter(url__contains="youtube").filter(url__contains="watch").order_by("?").first()
