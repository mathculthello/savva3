from django.contrib.sitemaps import Sitemap
from .models import Video

class BaseSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Video.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
