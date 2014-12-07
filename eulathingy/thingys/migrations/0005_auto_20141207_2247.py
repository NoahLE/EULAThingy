# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thingys', '0004_remove_thingysection_section_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThingyDocs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc_rating', models.IntegerField(default=0, max_length=1)),
                ('doc_company', models.IntegerField(max_length=250, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThingyStrings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc_title', models.CharField(max_length=250, verbose_name=b'Document title.')),
                ('string_rating', models.IntegerField(default=0, max_length=1, null=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='thingysection',
            name='thingy',
        ),
        migrations.DeleteModel(
            name='Thingy',
        ),
        migrations.RemoveField(
            model_name='thingysentence',
            name='thingy_section',
        ),
        migrations.DeleteModel(
            name='ThingySection',
        ),
        migrations.DeleteModel(
            name='ThingySentence',
        ),
        migrations.AddField(
            model_name='thingydocs',
            name='doc_title',
            field=models.ForeignKey(to='thingys.ThingyStrings'),
            preserve_default=True,
        ),
    ]
