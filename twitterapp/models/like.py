from django.db import models


class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000, null=False)
    owner = models.ForeignKey('auth.User', related_name='tweets', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']
        