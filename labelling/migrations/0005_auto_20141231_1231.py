# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0004_auto_20141230_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteruser',
            name='description',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
    ]
