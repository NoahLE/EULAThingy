# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('thingys', '0010_auto_20141208_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='thingystring',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 8, 3, 51, 52, 918189, tzinfo=utc), auto_now=True, db_index=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='thingystring',
            name='rating',
            field=models.IntegerField(default=0, max_length=1, null=True),
            preserve_default=True,
        ),
    ]
