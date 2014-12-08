# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thingys', '0007_auto_20141208_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thingydoc',
            old_name='rating_votes',
            new_name='doc_votes',
        ),
        migrations.RenameField(
            model_name='thingystring',
            old_name='rating_votes',
            new_name='string_votes',
        ),
    ]
