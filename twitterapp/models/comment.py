from django.db import models
from .tweet import Tweet


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey('Tweet', related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='tweets_comment', on_delete=models.CASCADE)
    content = models.CharField(max_length=1000, null=False)

    class Meta:
        ordering = ['created_at']
        