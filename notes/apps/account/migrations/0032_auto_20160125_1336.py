# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0031_auto_20160122_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 13, 36, 57, 790260, tzinfo=utc)),
        ),
    ]
