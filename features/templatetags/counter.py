from django import template
from features.models import Counter

register = template.Library()

@register.simple_tag(takes_context=True)
def counter(context):
	url=context.request.path
	if not context.request.user.is_staff:
		c=Counter()
		c.url=url
		c.save()
	return Counter.objects.filter(url=url).count()
