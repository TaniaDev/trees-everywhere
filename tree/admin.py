from django.contrib import admin

from tree.models import PlantedTree, Tree

admin.site.register([PlantedTree, Tree])
