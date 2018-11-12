# cookbook/ingredients/schema.py
import graphene



from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


from .models import Resource, Tag, Area, Video

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


class VideoNode(DjangoObjectType):
    get_absolute_url = graphene.String()

    def resolve_get_absolute_url(self, _args, *_kwargs):
        return self.get_absolute_url()

    class Meta:
        model = Video
        filter_fields = {
        'id': ['exact'],
        'url': ['contains'],
        'title': ['contains'],
        'areas': ['exact'],
        }
        interfaces = (graphene.relay.Node, )

class VideoType(DjangoObjectType):
    class Meta:
        model = Video

class Query(object):
    url = graphene.relay.Node.Field(VideoNode)
    all_urls = DjangoFilterConnectionField(VideoNode)

    tag = graphene.relay.Node.Field(TagNode)
    all_tags = DjangoFilterConnectionField(TagNode)

    area = graphene.relay.Node.Field(AreaNode)
    all_areas = DjangoFilterConnectionField(AreaNode)
    #all_areas = graphene.Field(AreaNode)

    random_url = graphene.Field(VideoType)

    def resolve_all_areas(self,info,**kwargs):
        # Выбираем только те темы, на которые есть видео
        return Area.objects.filter(resource__video__isnull=False).distinct()

    def resolve_random_url(self,info,**kwargs):
        return Video.objects.filter(url__contains="youtube").filter(url__contains="watch").order_by("?").first()
