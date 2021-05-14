import utilities as utl
import matplotlib.pyplot as plt
filename = '../data/temperatures_clean.csv'


def plot_temp(data):
	x = []
	y = []
	tmp = [1, 2, 3, 4, 5, 6, 7, 8]
	for k, v in data.items():
		x.append(k)
		y.append(v)
	plt.violinplot(y)
	plt.xticks(tmp, x)
	plt.xlabel('country')
	plt.ylabel('Average Temperature Celsius')
	plt.title('distribution of temperatures within each country')
	plt.grid(zorder=0)
	plt.savefig('image7.png')
	plt.close()


if __name__ == '__main__':
	plot_temp(utl.data_parser_dict(filename))
