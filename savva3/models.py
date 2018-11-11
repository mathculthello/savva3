from django.db import models

class Meta(models.Model):
    slug = models.CharField(max_length=40)
    keywords_string = models.CharField(max_length=500)
    description = models.TextField()

    def keywords(self):
        string=self.keywords_string

        return [x.strip() for x in string.split(",")]

    def __str__(self):
        return self.slug


class Setting(models.Model):
    key = models.CharField(max_length=50, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key
