# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20150609_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 9, 12, 39, 34, 341879, tzinfo=utc)),
        ),
    ]
