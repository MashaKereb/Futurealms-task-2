# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chathistory',
            old_name='answer',
            new_name='answers',
        ),
        migrations.RemoveField(
            model_name='chathistory',
            name='question',
        ),
        migrations.AddField(
            model_name='chathistory',
            name='answers_number',
            field=models.SmallIntegerField(default=0),
        ),
    ]
