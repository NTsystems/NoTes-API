# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20150422_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
        ),
    ]
