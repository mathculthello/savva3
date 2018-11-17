from django.db import models

# Create your models here.

class Formulae(models.Model):
    formulae = models.CharField(max_length=1000)
    published = models.BooleanField(default=False)

class Counter(models.Model):
    visit_date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=200, blank=True)
