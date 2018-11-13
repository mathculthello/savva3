# Suppose you have `myapp` application.
# In its `models.py` you define your customized models.
from sitetree.models import TreeItemBase, TreeBase
from django.db import models
from meta.models import ModelMeta


class MyTreeItem(ModelMeta, TreeItemBase):
    """And that's a tree item model with additional `css_class` field."""
    rel = models.CharField('Rel', blank=True, max_length=50)
    _keywords = models.CharField(max_length=200, blank=True)
    head_title = models.CharField(max_length=200, blank=True)

    def keywords(self):
        string=self._keywords

        return [x.strip() for x in string.split(",")]

    _metadata = {
        'title':'title',
        'keywords':'keywords',
        'description': 'description'
    }
