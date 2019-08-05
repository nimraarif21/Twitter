from django.db import models
from .tweet import Tweet


class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey('Tweet', related_name='likes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']
        