import utilities as utl
import matplotlib.pyplot as plt
filename = '../data/temperatures_clean.csv'


def plot_temp(xy):
	x = xy[0]
	y = xy[1]
	plt.scatter(x, y, marker='.', zorder=3, alpha=0.1)
	plt.xlabel('year')
	plt.ylabel('Average Temperature Celsius')
	plt.title('AverageTemperatureCelsius vs. year')
	plt.grid(zorder=0)
	plt.savefig('image3.png')
	plt.close()


if __name__ == '__main__':
	plot_temp(utl.data_parser_list(filename))
