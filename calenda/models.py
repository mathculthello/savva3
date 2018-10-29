from django.db import models

# Create your models here.



class Event(models.Model):
    title = models.CharField(max_length=500, null=True)
    start = models.DateTimeField()
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=300, blank=True)

    place = models.CharField(max_length=300, blank=True)

    comment = models.TextField(blank=True)

    def __str__(self):
        return self.title
