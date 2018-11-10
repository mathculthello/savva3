
# Import two helper functions and two admin models to inherit our custom model from.
from sitetree.admin import TreeItemAdmin, TreeAdmin, override_tree_admin, override_item_admin

# This is our custom tree admin model.
class CustomTreeAdmin(TreeAdmin):
    pass
    #exclude = ('title',)  # Here we exclude `title` field from form.

# And our custom tree item admin model.
class CustomTreeItemAdmin(TreeItemAdmin):
    # That will turn a tree item representation from the default variant
    # with collapsible groupings into a flat one.
    fieldsets= None

# Now we tell the SiteTree to replace generic representations with custom.
override_tree_admin(CustomTreeAdmin)
override_item_admin(CustomTreeItemAdmin)
