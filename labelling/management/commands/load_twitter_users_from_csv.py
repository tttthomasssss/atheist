__author__ = 'thomas'
import csv

from django.core.management.base import BaseCommand

from dateutil import parser

from ...models import TwitterUser


class Command(BaseCommand):
	def handle(self, *args, **options):
		with open(args[0], 'rb') as csv_file:
			csv_reader = csv.reader(csv_file)
			for idx, row in enumerate(csv_reader):
				TwitterUser.objects.create(
					user_id = int(row[0]) if row[0] is not None and row[0] != '' else None,
					created_at = parser.parse(row[1]) if row[1] is not None and row[1] != '' else None,
					description = row[2],
					lang = row[3],
					geo_enabled = int(row[4]) if row[4] is not None and row[4] != '' else None,
					location = row[5],
					time_zone = row[6],
					utc_offset = int(row[7]) if row[7] is not None and row[7] != '' else None,
					name = row[8],
					screen_name = row[9],
					url = row[10],
					statuses_count = int(row[11]) if row[11] is not None and row[11] != '' else None,
					followers_count = int(row[12]) if row[12] is not None and row[12] != '' else None,
					default_profile = int(row[13]) if row[13] is not None and row[13] != '' else None,
					default_profile_image = int(row[14]) if row[14] is not None and row[14] != '' else None,
					entities = row[15],
					favourites_count = int(row[16]) if row[16] is not None and row[16] != '' else None,
					friends_count = int(row[17]) if row[17] is not None and row[17] != '' else None,
					listed_count = int(row[18]) if row[18] is not None and row[18] != '' else None,
					profile_background_color = row[19],
					profile_background_image_url = row[20],
					profile_background_image_url_https = row[21],
					profile_banner_url = row[22],
					profile_image_url = row[23],
					profile_image_url_https = row[24],
				)

				if (idx % 1000 == 0):
					print '%d Users created!' % (idx,)