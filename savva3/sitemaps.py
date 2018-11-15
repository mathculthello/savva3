from events.sitemap import EventSitemap
from base.sitemap import VideoSitemap
from django.contrib.sitemaps import Sitemap
from savva_menu.models import MyTreeItem as Pages

class PagesSitemap(Sitemap):

    def items(self):
        return Pages.objects.all()

    def changefreq(self, obj):
        return obj.changefreq

    def priority(self,obj):
        return obj.priority

sitemaps = {
'base': VideoSitemap,
'events': EventSitemap,
'pages': PagesSitemap,
}
