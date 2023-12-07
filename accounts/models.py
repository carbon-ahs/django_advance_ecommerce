# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_permissions+",  # Provide a unique related_name
    )
