
from django.db import models
from meta.models import ModelMeta
from django.utils import timezone as tz



class MetaClass(ModelMeta, models.Model):
    ''' Класс, содержащий дополнительную информацию для поисковиков '''
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    updated_at=models.DateTimeField(auto_now=True, blank=False)
    keywords = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)

    def date_field(self):
        return self.updated_at
        
    def get_keywords(self):
        return [x.strip() for x in self.keywords.split(',')]


    def get_description(self):
        return self.description


    class Meta:
        abstract=True

    _metadata = {
        'description': 'get_description',
        'keywords': 'get_keywords'
    }