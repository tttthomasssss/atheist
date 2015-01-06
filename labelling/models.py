from django.db import models


class TwitterUser(models.Model):
	user_id									= models.IntegerField(default=0)
	created_at								= models.DateTimeField(blank=True, null=True)
	description								= models.CharField(max_length=2000, blank=True, null=True)
	description_length						= models.PositiveIntegerField(default=0)
	lang									= models.CharField(max_length=10, blank=True, null=True)
	geo_enabled								= models.IntegerField(default=0)
	location								= models.CharField(max_length=40, blank=True, null=True)
	time_zone								= models.CharField(max_length=60, blank=True, null=True)
	utc_offset								= models.IntegerField(default=0)
	name									= models.CharField(max_length=60, blank=True, null=True)
	screen_name								= models.CharField(max_length=60, blank=True, null=True)
	url										= models.URLField(max_length=500, blank=True, null=True)
	statuses_count							= models.IntegerField(default=0)
	followers_count							= models.IntegerField(default=0)
	default_profile							= models.IntegerField(default=0)
	default_profile_image					= models.IntegerField(default=0)
	entities								= models.TextField(blank=True, null=True)
	favourites_count						= models.IntegerField(default=0)
	friends_count							= models.IntegerField(default=0)
	listed_count							= models.IntegerField(default=0)
	profile_background_color				= models.CharField(max_length=10, blank=True, null=True)
	profile_background_image_url			= models.URLField(max_length=500, blank=True, null=True)
	profile_background_image_url_https		= models.URLField(max_length=500, blank=True, null=True)
	profile_banner_url						= models.URLField(max_length=500, blank=True, null=True)
	profile_image_url						= models.URLField(max_length=500, blank=True, null=True)
	profile_image_url_https					= models.URLField(max_length=500, blank=True, null=True)
	profile_image							= models.ImageField(max_length=1000, upload_to='profile_images', blank=True, null=True)
	profile_image_height					= models.PositiveIntegerField(default=0)
	profile_image_width						= models.PositiveIntegerField(default=0)

	def save(self, *args, **kwargs):
		self.description_length = len(self.description)
		return super(TwitterUser, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.screen_name


class Labelling(models.Model):
	label_group_name	= models.CharField(max_length=500, blank=True, null=True)
	label 				= models.IntegerField(default=0)
	label_description	= models.CharField(max_length=500, blank=True, null=True)

	def __unicode__(self):
		return '%s: %d' % (self.label_group_name, self.label)


class UserLabelling(models.Model):
	label 	= models.ForeignKey(Labelling)
	user 	= models.ForeignKey(TwitterUser)

	def __unicode__(self):
		return '%s -> [%s]' % (self.user, self.label)