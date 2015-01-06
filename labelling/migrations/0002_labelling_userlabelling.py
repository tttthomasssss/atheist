# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labelling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label_group_name', models.CharField(max_length=500, null=True, blank=True)),
                ('label', models.IntegerField(default=0)),
                ('label_description', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLabelling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.ForeignKey(to='labelling.Labelling')),
                ('user', models.ForeignKey(to='labelling.TwitterUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
