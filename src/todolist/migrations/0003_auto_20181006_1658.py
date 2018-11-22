# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todolist_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='description',
            field=models.CharField(max_length=200, blank=True, help_text='max 200 letters'),
        ),
    ]
