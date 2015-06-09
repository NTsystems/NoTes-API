# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_userprofile_activation_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='activation_key',
        ),
        migrations.AddField(
            model_name='user',
            name='activation_key',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 9, 10, 41, 43, 505386, tzinfo=utc)),
        ),
    ]
