# cookbook/ingredients/schema.py
import graphene



from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


from .models import Url, Tag, Area

class TagNode(DjangoObjectType):
    class Meta:
        model=Tag
        filter_fields=['title','urls']
        interfaces=(graphene.relay.Node, )

class AreaNode(DjangoObjectType):
    class Meta:
        model=Area
        filter_fields=['title','urls']
        interfaces=(graphene.relay.Node, )


class UrlNode(DjangoObjectType):
    class Meta:
        model = Url
        filter_fields = {
        'id': ['exact'],
        'url': ['exact', 'contains'],
        'title': ['contains'],
        'areas': ['exact'],
        'many_tag': ['exact'],
        'many_tag__name': ['exact']
        }
        interfaces = (graphene.relay.Node, )

class UrlType(DjangoObjectType):
    class Meta:
        model = Url

class Query(object):
    url = graphene.relay.Node.Field(UrlNode)
    all_urls = DjangoFilterConnectionField(UrlNode)

    tag = graphene.relay.Node.Field(TagNode)
    all_tags = DjangoFilterConnectionField(TagNode)

    area = graphene.relay.Node.Field(AreaNode)
    all_areas = DjangoFilterConnectionField(AreaNode)

    random_url = graphene.Field(UrlType)

    def resolve_random_url(serlf,info,**kwargs):
        return Url.objects.filter(url__contains="youtube").filter(url__contains="watch").order_by("?").first()
