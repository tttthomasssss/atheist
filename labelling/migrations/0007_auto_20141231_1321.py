# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0006_twitteruser_description_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteruser',
            name='profile_image_height',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='twitteruser',
            name='profile_image_width',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
