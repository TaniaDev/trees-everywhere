from django.db import models


class Tree(models.Model):
    name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=50)

    def __str__(self):
        return f"Name: {self.name}"


class PlantedTree(models.Model):
    age = models.IntegerField()
    planted_at = models.DateTimeField()
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)
    account = models.ForeignKey("account.Account", on_delete=models.CASCADE, null=True)
    tree = models.ForeignKey("tree.Tree", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Tree: {self.tree}"
