from django.db import models
from .tweet import Tweet


class TweetLike(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey('Tweet', related_name='likes', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='tweets_liked', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tweet', 'owner',)
        ordering = ['created_at']
        