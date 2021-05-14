import utilities as utl
import matplotlib.pyplot as plt
import numpy as np
filename = '../data/temperatures_clean.csv'


def plot_temp(data):
	x = []
	y = []
	sx = []
	sy = []
	tmp = [1, 2, 3, 4, 5, 6, 7, 8]
	for k, v in data.items():
		x.append(k)
		y.append(v)
		sy.extend(v)
		for i in v:
			sx.append(k)
	medianprops = dict(color='black')
	plt.boxplot(y, zorder=3, medianprops=medianprops)
	for i in tmp:
		tmpi = np.random.normal(i, 0.08, size=len(y[i-1]))
		plt.scatter(tmpi, y[i-1], alpha=0.15, color='red', marker='.')
	plt.xticks(tmp, x)
	plt.xlabel('country')
	plt.ylabel('Average Temperature Celsius')
	plt.title('distribution of temperatures within each country')
	plt.grid(zorder=0)
	plt.savefig('image6.png')
	plt.close()


if __name__ == '__main__':
	plot_temp(utl.data_parser_dict(filename))
