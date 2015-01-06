# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0005_auto_20141231_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteruser',
            name='description_length',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
