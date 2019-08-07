from django.db import models
from .tweet import Tweet


class InvalidToken(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=1000, null=False)

    class Meta:
        ordering = ['created_at']

        