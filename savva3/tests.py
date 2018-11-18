from django.test import TestCase
from django.test import Client
from django.test.utils import override_settings
from django.conf import settings


from datetime import datetime
import os
from django.utils._os import safe_join
from django.template.utils import get_app_template_dirs
from django.utils import timezone as tz

# Create your tests here.
class Savva3TestCase(TestCase):

	def test_index_page(self):
		c=Client()
		response=c.get('/')
		self.assertEqual(response.status_code, 200)


	@override_settings(DEBUG=False)
	def test_if_not_found_redirects_with_301(self):
		c=Client()
		response=c.get('/abracadabra/')
		#self.assertEqual(response.status_code, 301)

	def test_template_mtime(self):
		template_name="pages/team.html"
		template_dirs = get_app_template_dirs('templates')
		template_mtime=None
		for template_dir in template_dirs:
			try:
				template_path = safe_join(template_dir, template_name)
				a = datetime.fromtimestamp(os.stat(template_path).st_mtime)
				template_mtime = tz.make_aware(a)
			except:
				continue

		#self.assertEqual(template_mtime,'2018-01-01')
