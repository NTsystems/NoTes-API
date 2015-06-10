# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20150609_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_key',
            field=models.CharField(default=b' ', max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 9, 11, 53, 43, 715047, tzinfo=utc)),
        ),
    ]
