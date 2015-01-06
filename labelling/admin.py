from django.contrib import admin

from .models import TwitterUser, Labelling, UserLabelling


class TwitterUserAdmin(admin.ModelAdmin):
	fields = [
		'user_id',
		'created_at',
		'description',
		'lang',
		'geo_enabled',
		'location',
		'time_zone',
		'utc_offset',
		'name',
		'screen_name',
		'url',
		'statuses_count',
		'followers_count',
		'default_profile',
		'default_profile_image',
		'entities',
		'favourites_count',
		'friends_count',
		'listed_count',
		'profile_background_color',
		'profile_background_image_url',
		'profile_background_image_url_https',
		'profile_banner_url',
		'profile_image_url',
		'profile_image_url_https',
		'profile_image'
	]


class LabellingAdmin(admin.ModelAdmin):
	fields = [
		'label_group_name',
		'label',
		'label_description'
	]


class UserLabellingAdmin(admin.ModelAdmin):
	fields = [
		'label',
		'user'
	]


admin.site.register(TwitterUser, TwitterUserAdmin)
admin.site.register(Labelling, LabellingAdmin)
admin.site.register(UserLabelling, UserLabellingAdmin)