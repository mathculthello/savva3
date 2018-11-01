from django.contrib import admin

# Register your models here.
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ['start', 'city', 'title']
    filter_horizontal = ['video']


admin.site.register(Event, EventAdmin)
