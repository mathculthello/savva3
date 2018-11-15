from django import template
from features.models import Counter
register = template.Library()

@register.simple_tag
def counter():
    c=Counter()
    c.save()
    return Counter.objects.count()
