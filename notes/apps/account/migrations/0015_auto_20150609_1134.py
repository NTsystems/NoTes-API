# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20150609_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key',
            field=models.CharField(default=b' ', max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 9, 11, 34, 51, 656456, tzinfo=utc)),
        ),
    ]
