from events.sitemap import EventSitemap
from base.sitemap import VideoSitemap
from django.contrib.sitemaps import Sitemap
from savva3.menu import TOP_MENU, BOTTOM_MENU

class PagesSitemap(Sitemap):

    def items(self):
    	return TOP_MENU+BOTTOM_MENU

    def changefreq(self, obj):
        return obj['changefreq']

    def priority(self,obj):
        return obj['priority']

    def location(self,obj):
    	return obj['url']

sitemaps = {
'base': VideoSitemap,
'events': EventSitemap,
'pages': PagesSitemap,
}
