from django.contrib import admin
from .models import Joke
# Register your models here.

class JokeAdmin(admin.ModelAdmin):
    list_display = ['title','author','published','date_added']


admin.site.register(Joke, JokeAdmin)
