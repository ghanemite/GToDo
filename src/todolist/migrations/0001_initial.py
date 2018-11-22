# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100, help_text='max 100 letters')),
                ('description', models.CharField(max_length=200, help_text='max 200 letters')),
                ('done', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('list_name', models.CharField(max_length=50, help_text='Enter list name max 50 characters')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.AddField(
            model_name='todoitem',
            name='parent',
            field=models.ForeignKey(related_name='items', to='todolist.TodoList'),
        ),
    ]
