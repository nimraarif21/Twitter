from django.db import models


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20, null=False, unique=True)
    email = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=20)

    class Meta:
        ordering = ['created']
