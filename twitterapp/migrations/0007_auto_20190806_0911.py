# Generated by Django 2.2.3 on 2019-08-06 09:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitterapp', '0006_auto_20190806_0809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrelation',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterUniqueTogether(
            name='userrelation',
            unique_together={('owner', 'following')},
        ),
    ]
