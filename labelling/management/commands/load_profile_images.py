__author__ = 'thomas'
import os
import urllib

from django.db.models import Q
from django.core.files import File
from django.core.management.base import BaseCommand

from labelling.models import TwitterUser


class Command(BaseCommand):
	def handle(self, *args, **options):
		print 'Downloading Profile Images for %d Users...' % (TwitterUser.objects.filter(~Q(profile_image_url=None)).count())
		for idx, user in enumerate(TwitterUser.objects.filter(~Q(profile_image_url=None))):
			result = urllib.urlretrieve(user.profile_image_url)
			user.profile_image.save(os.path.basename(user.profile_image_url), File(open(result[0])))
			user.save()

			if (idx % 1000 == 0):
				print 'Images for %d Users set!' % (idx,)