from rest_framework import generics

from tree.models import PlantedTree
from tree.serializers import PlantedTreeSerializer


# Create your views here.
class PlantedTreeList(generics.ListCreateAPIView):
    serializer_class = PlantedTreeSerializer

    def get_queryset(self):
        queryset = PlantedTree.objects.filter(user=self.request.user)
        return queryset
