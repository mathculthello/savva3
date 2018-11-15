from django.contrib.sitemaps import Sitemap
from .models import Video


class ItemSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.7

	def lastmod(self, obj):
		return obj.updated_at

class VideoSitemap(ItemSitemap):
	def items(self):
		return Video.objects.all()