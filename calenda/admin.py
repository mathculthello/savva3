from django.contrib import admin

# Register your models here.
from .models import Event


class CalendAdmin(admin.ModelAdmin):
    list_display = ['start', 'city', 'title']


admin.site.register(Event, CalendAdmin)
