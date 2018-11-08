from django.contrib.sitemaps import Sitemap
from events.models import Event

class EventSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
