# Suppose you have `myapp` application.
# In its `models.py` you define your customized models.
from sitetree.models import TreeItemBase, TreeBase
from django.db import models

class MyTreeItem(TreeItemBase):
    """And that's a tree item model with additional `css_class` field."""
    rel = models.CharField('Rel', blank=True, max_length=50)
