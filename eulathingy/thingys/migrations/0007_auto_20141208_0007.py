# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thingys', '0006_auto_20141208_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='thingydoc',
            name='rating_votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thingystring',
            name='rating_votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
