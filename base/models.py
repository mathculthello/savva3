from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=500, null=True)
    tag = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
