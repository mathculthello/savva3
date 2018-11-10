from django.db import models

class Meta(models.Model):
    slug = models.CharField(max_length=40)
    keywords_string = models.CharField(max_length=500)
    description = models.TextField()

    def keywords(self):
        string=self.keywords_string

        return [x.strip() for x in string.split(",")]
