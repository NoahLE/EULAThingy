# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThingyDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Document title.', max_length=250)),
                ('rating', models.IntegerField(max_length=1, db_index=True, default=0)),
                ('votes', models.IntegerField(default=0)),
                ('category', models.IntegerField(db_index=True, default=0, choices=[(0, 'Other'), (1, 'Health'), (2, 'Technology'), (3, 'Finance'), (4, 'Service')])),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThingyString',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('string', models.TextField()),
                ('rating', models.IntegerField(max_length=1, null=True, default=0)),
                ('votes', models.IntegerField(default=0)),
                ('last_updated', models.DateTimeField(db_index=True, auto_now=True)),
                ('doc', models.ForeignKey(to='thingys.ThingyDoc')),
            ],
        ),
    ]
