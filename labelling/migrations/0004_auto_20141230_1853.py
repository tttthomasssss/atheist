# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0003_twitteruser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteruser',
            name='profile_image',
            field=models.ImageField(max_length=1000, null=True, upload_to=b'profile_images', blank=True),
        ),
    ]
