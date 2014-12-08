# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thingys', '0008_auto_20141208_0036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thingydoc',
            old_name='doc_rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='thingydoc',
            old_name='doc_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='thingydoc',
            old_name='doc_votes',
            new_name='votes',
        ),
        migrations.RenameField(
            model_name='thingystring',
            old_name='string_rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='thingystring',
            old_name='string_votes',
            new_name='votes',
        ),
        migrations.RemoveField(
            model_name='thingydoc',
            name='doc_company',
        ),
    ]
