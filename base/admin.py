from django.contrib import admin
from .models import Url
# Register your models here.
from django.utils.html import format_html



class UrlAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'tag')
    def link(self,obj):
        return format_html("<a target='_blank' href='{url}'>{url}</a>", url=obj.url)




admin.site.register(Url, UrlAdmin)
