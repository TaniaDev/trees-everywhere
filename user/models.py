from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return f"Username: {self.username}"


class Profile(models.Model):
    about = models.TextField(blank=True)
    joined = models.DateTimeField(auto_now_add=True)
