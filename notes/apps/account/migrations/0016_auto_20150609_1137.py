# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20150609_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='activation_key',
        ),
        migrations.RemoveField(
            model_name='user',
            name='key_expires',
        ),
    ]
