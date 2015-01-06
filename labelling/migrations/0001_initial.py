# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('lang', models.CharField(max_length=10, null=True, blank=True)),
                ('geo_enabled', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=40, null=True, blank=True)),
                ('time_zone', models.CharField(max_length=60, null=True, blank=True)),
                ('utc_offset', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=60, null=True, blank=True)),
                ('screen_name', models.CharField(max_length=60, null=True, blank=True)),
                ('url', models.URLField(max_length=500, null=True, blank=True)),
                ('statuses_count', models.IntegerField(default=0)),
                ('followers_count', models.IntegerField(default=0)),
                ('default_profile', models.IntegerField(default=0)),
                ('default_profile_image', models.IntegerField(default=0)),
                ('entities', models.TextField(null=True, blank=True)),
                ('favourites_count', models.IntegerField(default=0)),
                ('friends_count', models.IntegerField(default=0)),
                ('listed_count', models.IntegerField(default=0)),
                ('profile_background_color', models.CharField(max_length=10, null=True, blank=True)),
                ('profile_background_image_url', models.URLField(max_length=500, null=True, blank=True)),
                ('profile_background_image_url_https', models.URLField(max_length=500, null=True, blank=True)),
                ('profile_banner_url', models.URLField(max_length=500, null=True, blank=True)),
                ('profile_image_url', models.URLField(max_length=500, null=True, blank=True)),
                ('profile_image_url_https', models.URLField(max_length=500, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
