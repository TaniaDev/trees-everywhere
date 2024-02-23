from rest_framework import serializers

from tree.models import PlantedTree


class PlantedTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantedTree
        fields = "__all__"
