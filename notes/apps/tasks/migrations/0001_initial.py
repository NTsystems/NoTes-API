# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('description', models.TextField(blank=True)),
                ('percentage', models.FloatField(default=0.0)),
                ('status', models.IntegerField(default=1, choices=[(1, b'New'), (2, b'In_progress'), (3, b'Done'), (4, b'Closed')])),
                ('asigned_to', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_by', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(to='tasks.Task'),
        ),
    ]
