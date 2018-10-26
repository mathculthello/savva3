from django.contrib import admin
from .models import *
# Register your models here.
from django.utils.html import format_html



class UrlAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'tag', 'tags',)
    search_fields = ('tag',)
    list_filter = ('many_tag','areas',)
    def link(self,obj):
        return format_html("<a target='_blank' href='{url}'>{url}</a>", url=obj.url)
    def tags(self,obj):
        x=''
        for a in obj.many_tag.all():
            x = x + a.name
        return x




admin.site.register(Url, UrlAdmin)
admin.site.register(Tag)
admin.site.register(Area)
