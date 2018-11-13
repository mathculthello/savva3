from .models import Setting
import logging
import sys
from .helpers import sttngs
from savva_menu.models import MyTreeItem as Menu

def meta(request):
    try:
        meta = Menu.objects.get(url=request.path)
        title = meta.head_title
        return {'meta':meta.as_meta(), 'title': title}
    except:
        return {}

def settings(request):
    return {'savva':sttngs}
