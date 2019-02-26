from django import template
register = template.Library()

@register.filter
def rating_type(obj):
    return obj._meta.label