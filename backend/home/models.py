from django.conf import settings
from django.db import models


class Student(models.Model):
    "Generated Model"
    firstname = models.TextField()
    email = models.EmailField(
        max_length=254,
    )
    username = models.TextField(
        null=True,
        blank=True,
    )
    password = models.TextField(
        null=True,
        blank=True,
    )
