from django.contrib import admin
from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = [
        "rating_type",
        "iid",
        "ip",
        "value",
        "date",
    ]


admin.site.register(Rating, RatingAdmin)
