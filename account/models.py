from django.db import models
from django.urls import reverse


class Account(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    users = models.ManyToManyField("user.User")

    def __str__(self):
        return str(self.name)
