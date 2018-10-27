from django.db import models
from embed_video import fields as video_fields


# Create your models here.
class AllMathTheme(models.Model):
    title = models.CharField(max_length=300, null=False, unique=True)
    depends = models.ManyToManyField('self', blank=True)
    def __str__(self):
            return self.title

class AllMathVideo(models.Model):
    number = models.IntegerField(null=False, default=0)
    video = video_fields.EmbedVideoField(null=True)
    title = models.CharField(max_length=500, null=False)
    theme = models.ManyToManyField(AllMathTheme, blank=True)
    def __str__(self):
        return self.title
