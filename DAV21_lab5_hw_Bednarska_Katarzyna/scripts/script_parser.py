import csv
file = '../data/temperature.csv'

def temp_cleaner(temp_file):
	with open(temp_file) as input_file:
		reader = csv.reader(input_file)
		header = ['record_id','month','year','AverageTemperature','AverageTemperatureUncertainty','City','country_id','Country','Latitude','Longitude']
		with open('../data/temperatures_clean.csv', 'w', newline='') as output_file:
			writer = csv.writer(output_file)
			writer.writerow(header)
			for line in reader:
				new_line=[]
				if line[0] == 'record_id':
					continue
				if line[6]=='' or line[6]=='NA':
					continue
				if line[8]=='' or line[8]=='NA':
					continue
				if line[4]=='NA':
					continue
				if line[5]=='NA':
					continue
				ATC = (float(line[4]) - 32 ) * 5/9
				ATUC = (float(line[5]) - 32) * 5/9
				new_line.extend([line[0],line[1],line[3],ATC,ATUC,line[6],line[7],line[8],line[9],line[10] ])
				writer.writerow(new_line)

if __name__ == '__main__':
	temp_cleaner(file)