__author__ = 'thomas'
import csv
import os
import shutil

import requests


def load_profile_image(url, django_id):
	try:
		print 'LOADING URL AT=%s; ID=%s' %(url, django_id)
		r = requests.get(url, stream=True, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0'})
		if (r.status_code == 200):
			fname = '%s_%s' % (django_id, os.path.basename(url))
			p = os.path.join('/Users/thomas/DevSandbox/InfiniteSandbox/tag-lab/atheist/temp', fname)
			with open(p, 'wb') as f:
				r.raw.decode_content = True
				shutil.copyfileobj(r.raw, f)
				print '		> SAVED FILE AT=%s' % (p,)
				return 1
	except:
		print 'OASCH!!'
	return 0


if (__name__ == '__main__'):
	with open('/Users/thomas/DevSandbox/EpicDataShelf/tag-lab/age_inf_timezone_london/profile_image_dump.csv', 'rb') as csv_file:
		csv_reader = csv.reader(csv_file)
		c = 0
		for row in csv_reader:
			if (c > 1500):
				break
			c += load_profile_image(row[1], row[0])

			if (c % 100 == 0):
				print '###### %d images loaded!!!' % (c,)