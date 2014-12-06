# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thingys', '0002_thingy_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThingySentence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name=b'Sentence content')),
                ('rating', models.IntegerField(default=0, verbose_name=b'The rating of this sentence')),
                ('thingy_section', models.ForeignKey(to='thingys.ThingySection')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
