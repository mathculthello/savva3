from django.db import models

# Create your models here.

class Formulae(models.Model):
    formulae = models.CharField(max_length=1000)
    published = models.BooleanField(default=False)
