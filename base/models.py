from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    title = models.CharField(max_length=100, null=False, default='')
    def __str__(self):
        return self.title

class Area(models.Model):
    name = models.CharField(max_length=500, unique=True, null=False)
    title = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title


# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=500, null=True)
    tag = models.CharField(max_length=100, null=True)
    many_tag = models.ManyToManyField(Tag,blank=True)
    areas = models.ManyToManyField(Area,blank=True)

    def __str__(self):
        return self.title

# Create your models here.
