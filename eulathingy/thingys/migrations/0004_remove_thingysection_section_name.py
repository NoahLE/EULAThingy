# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thingys', '0003_thingysentence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thingysection',
            name='section_name',
        ),
    ]
