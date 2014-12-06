# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thingy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=200, null=True)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThingySection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_name', models.CharField(max_length=50, null=True)),
                ('content', models.TextField()),
                ('thingy', models.ForeignKey(to='thingys.Thingy')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
