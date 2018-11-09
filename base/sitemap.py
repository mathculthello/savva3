from django.contrib.sitemaps import Sitemap
from .models import Url

class UrlSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return Url.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
