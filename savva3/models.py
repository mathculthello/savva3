
from django.db import models
from meta.models import ModelMeta
from django.utils import timezone as tz



class MetaClass(ModelMeta, models.Model):
    ''' Класс, содержащий дополнительную информацию для поисковиков '''
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    updated_at=models.DateTimeField(auto_now=True, blank=False)
    _keywords = models.CharField(max_length=500, blank=True)

    def date_field(self):
        return self.updated_at
    def get_keywords(self):
        return [x.strip() for x in self._keywords.split(',')]
    class Meta:
        abstract=True