from .models import Meta, Setting
import logging
import sys
from .helpers import sttngs

logger = logging.getLogger(__name__)

def meta(request):
    meta = Meta.objects.filter(slug=request.path).first()
    return {'meta':meta}

def settings(request):
    return {'savva':sttngs}
