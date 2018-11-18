from datetime import datetime
import os
from django.utils._os import safe_join
from django.template.utils import get_app_template_dirs
from django.utils import timezone as tz
from savva3.models import MetaClass


def template_mtime(template_name):
	template_dirs = get_app_template_dirs('templates')
	template_mtime=None
	for template_dir in template_dirs:
		try:
			template_path = safe_join(template_dir, template_name)
			template_mtime = datetime.fromtimestamp(os.stat(template_path).st_mtime)
			template_mtime = tz.make_aware(template_mtime)
		except:
			continue

	return template_mtime



def model_mtime(model: MetaClass):
	try:
		return model.objects.order_by('-updated_at').first().updated_at
	except:
		return None
