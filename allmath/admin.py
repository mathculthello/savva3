from django.contrib import admin
from .models import AllMathVideo, AllMathTheme
from embed_video.admin import AdminVideoMixin

# Register your models here.

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(AllMathTheme)
admin.site.register(AllMathVideo, MyModelAdmin)
