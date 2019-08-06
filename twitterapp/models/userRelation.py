from django.db import models


class UserRelation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    following = models.ForeignKey('auth.User', related_name='following', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('owner', 'following',)
        ordering = ['created_at']