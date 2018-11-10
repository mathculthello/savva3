from .models import Meta
import logging
import sys

logger = logging.getLogger(__name__)

def meta(request):
    meta = Meta.objects.filter(slug=request.path).first()
    return {'meta':meta}
