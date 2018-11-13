from django.db import models

class Setting(models.Model):
    key = models.CharField(max_length=50, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key
