# map_points: data_id, date, category, latitude, longitude

from datetime import datetime


def convert_date(datestring):
	return datetime.strptime(datestring, '%b %d %Y %I:%M%p')



def convert_to_json(lineEntry):
	

with open('data.txt') as f:
	lines = f.readlines()
	print lines

for entry in lines:
	convert_to_json(entry)
