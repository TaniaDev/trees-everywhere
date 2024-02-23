from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    accounts = models.ManyToManyField("account.Account")

    def __str__(self):
        return str(self.username)


class Profile(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, null=True)
    about = models.TextField(blank=True)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
