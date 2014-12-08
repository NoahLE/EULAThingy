# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thingys', '0005_auto_20141207_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThingyDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc_title', models.CharField(max_length=250, verbose_name=b'Document title.')),
                ('doc_rating', models.IntegerField(default=0, max_length=1)),
                ('doc_company', models.IntegerField(max_length=250, blank=True)),
                ('category', models.IntegerField(default=0, db_index=True, choices=[(0, b'Other'), (1, b'Health'), (2, b'Technology'), (3, b'Finance'), (4, b'Service')])),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThingyString',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string', models.CharField(max_length=500)),
                ('string_rating', models.IntegerField(default=0, max_length=1, null=True)),
                ('doc', models.ForeignKey(to='thingys.ThingyDoc')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='thingydocs',
            name='doc_title',
        ),
        migrations.DeleteModel(
            name='ThingyDocs',
        ),
        migrations.DeleteModel(
            name='ThingyStrings',
        ),
    ]
