# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0002_labelling_userlabelling'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteruser',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=b'profile_images', blank=True),
            preserve_default=True,
        ),
    ]
