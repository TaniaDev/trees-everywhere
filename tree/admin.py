from django.contrib import admin

from tree.models import PlantedTree, Tree


class PlantedTreeAdmin(admin.ModelAdmin):
    list_display = ("tree", "age", "user")
    actions = ["activate_accounts", "deactivate_accounts"]


admin.site.register(PlantedTree, PlantedTreeAdmin)
admin.site.register(Tree)
