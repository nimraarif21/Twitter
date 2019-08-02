from django.db import models


class Userrelation(models.Model):
    createdat = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    following = models.ForeignKey('auth.User', related_name='following', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'following',)
        ordering = ['createdat']