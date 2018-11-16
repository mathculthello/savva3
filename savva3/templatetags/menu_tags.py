from django import template
from savva3.menu import TOP_MENU, BOTTOM_MENU
register = template.Library()

@register.inclusion_tag('menu/top.html', takes_context=True)
def topmenu(context):
	return {'request':context.request, 'menu':TOP_MENU};


@register.inclusion_tag('menu/bottom.html', takes_context=True)
def bottom_menu(context):
	return {'request':context.request, 'menu':BOTTOM_MENU};