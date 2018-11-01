from django.contrib import admin

# Register your models here.
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ['start', 'city', 'title', 'has_video']
    filter_horizontal = ['video']

    def has_video(self,obj):
        if(obj.video.count()>0):
            return True
        else:
            return False

    has_video.boolean=True


admin.site.register(Event, EventAdmin)
