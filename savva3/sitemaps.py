from events.sitemap import EventSitemap
from base.sitemap import VideoSitemap
from django.contrib.sitemaps import Sitemap
from savva3.menu import TOP_MENU, BOTTOM_MENU
from django.utils import timezone

class PagesSitemap(Sitemap):

	def items(self):
		return TOP_MENU+BOTTOM_MENU

	def changefreq(self, obj):
		return obj['changefreq']

	def priority(self,obj):
		return obj['priority']

	def location(self,obj):
		return obj['url']

	def lastmod(self,obj):
		try:
			return obj['lastmod']
		except:
			return None

sitemaps = {
'base': VideoSitemap,
'events': EventSitemap,
'pages': PagesSitemap,
}
