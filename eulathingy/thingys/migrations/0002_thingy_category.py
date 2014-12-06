# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thingys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thingy',
            name='category',
            field=models.IntegerField(default=0, db_index=True, choices=[(0, b'Other'), (1, b'Health'), (2, b'Technology'), (3, b'Finance'), (4, b'Service')]),
            preserve_default=True,
        ),
    ]
