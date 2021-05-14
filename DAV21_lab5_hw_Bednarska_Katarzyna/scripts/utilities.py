import csv


def data_parser_list(filename):
	"""
	:param filename: csv data file
	:return: list of lists of x(year) and y(temp) parameters
	"""
	x = []
	y = []
	with open(filename) as input_file:
		reader = csv.reader(input_file)
		for line in reader:
			if line[0] == 'record_id':
				pass
			else:
				x.append(round(float(line[2]),2))
				y.append(round(float(line[3]),2))
		return [x, y]


def data_parser_dict(filename):
	"""
	:param filename: csv data file
	:return: dict{country:[temp list]}
	"""
	data = {}
	with open(filename) as input_file:
		reader = csv.reader(input_file)
		for line in reader:
			if line[0] == 'record_id':
				pass
			else:
				if line[6] in data.keys():
					data[line[6]].append(round(float(line[3]),2))
				else:
					data[line[6]] = [round(float(line[3]),2)]
		return data

#todo: zrobic tutaj funkcje przerabiania danych na nastepny rodzaj