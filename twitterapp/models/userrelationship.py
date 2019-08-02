from django.db import models


class Userrelationship(models.Model):
    createdat = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    follower = models.ForeignKey('auth.User', related_name='follower', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'follower',)
        ordering = ['createdat']
