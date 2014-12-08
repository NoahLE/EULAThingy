# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thingys', '0009_auto_20141208_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thingystring',
            name='rating',
            field=models.IntegerField(default=0, max_length=1, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thingystring',
            name='string',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
