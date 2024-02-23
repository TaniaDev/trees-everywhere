from datetime import datetime

from django.db import models
from django.db.models import ExpressionWrapper, F, Func


class Tree(models.Model):
    name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class YearsDiff(Func):
    function = "EXTRACT"
    template = "%(function)s(YEAR FROM %(expressions)s)"
    output_field = models.IntegerField()


class PlantedTree(models.Model):
    planted_at = models.DateTimeField()
    age = ExpressionWrapper(YearsDiff(datetime.now(), F("planted_at")), output_field=models.IntegerField())
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)
    account = models.ForeignKey("account.Account", on_delete=models.CASCADE, null=True)
    tree = models.ForeignKey("tree.Tree", on_delete=models.CASCADE, null=True)
    latitude_location = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    longitude_location = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    def __str__(self):
        return str(self.tree)

    def get_planted_tree_location(self, planted_tree):
        return (planted_tree.latitude_location, planted_tree.longitude_location)
