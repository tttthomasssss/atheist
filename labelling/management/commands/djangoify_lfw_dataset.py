__author__ = 'thomas'
import os

from django.core.files import File
from django.core.management.base import BaseCommand

from common import paths

from labelling.models import TwitterUser


class Command(BaseCommand):
	def handle(self, *args, **options):
		count = 0
		verbose = (len(args) > 0 and args[0] == 'True')
		for folder in filter(lambda fx: True if not fx.startswith('.') and os.path.isdir(os.path.join(paths.get_dataset_path(), 'lfw_funneled', fx)) else False, os.listdir(os.path.join(paths.get_dataset_path(), 'lfw_funneled'))):
			if (verbose):
				print 'Folder:', folder
			for f in filter(lambda x: True if not x.startswith('.') and not os.path.isdir(os.path.join(paths.get_dataset_path(), 'lfw_funneled', folder, x)) else False, os.listdir(os.path.join(paths.get_dataset_path(), 'lfw_funneled', folder))):
				if (verbose):
					print '\tFile:', f
				django_file = File(open(os.path.join(paths.get_dataset_path(), 'lfw_funneled', folder, f)))

				user = TwitterUser.objects.create(user_id=-666, description='')
				user.profile_image.save(f, django_file)
				user.save()
				count += 1

				if (count % 100 == 0):
					print '%d users created!' % (count,)

		print 'Finished with %d users created!' % (count,)