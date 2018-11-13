# Suppose you have `myapp` application.
# In its `models.py` you define your customized models.
from sitetree.models import TreeItemBase, TreeBase
from django.db import models
from meta.models import ModelMeta


class MyTreeItem(ModelMeta, TreeItemBase):
    """And that's a tree item model with additional `css_class` field."""
    rel = models.CharField('Rel', blank=True, max_length=50)
    keywords_string = models.CharField(max_length=200, blank=True)
    head_title = models.CharField(max_length=200, blank=True)
    changefreq = models.CharField(max_length=10,blank=False,default="daily")
    priority = models.FloatField(null=False, default=1)

    def keywords(self):
        string=self.keywords_string

        return [x.strip() for x in string.split(",")]

    def get_absolute_url(self):
        return self.url

    _metadata = {
        'title':'title',
        'keywords':'keywords',
        'description': 'description'
    }
