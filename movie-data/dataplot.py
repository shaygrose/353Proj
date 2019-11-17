import pandas as pd
import matplotlib.pyplot as plt
import sys

data = pd.read_csv(sys.argv[1])

title = data['title']
director = data['director']
genre = data['genre']
rating = data['rating']
year = data['year']
gross = data['gross']
runtime = data['runtime']

def plot_fig(x_axis, y_axis, title, xlabel, ylabel):
    x = x_axis
    y = y_axis
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, '.b', alpha=0.2)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    ax1 = plt.axes()
    x_axis = ax1.axes.get_xaxis()
    x_axis.set_visible(False)

    

plot_fig(title, rating, 'Title vs. Rating', 'Title', 'Rating')
plot_fig(director, rating, 'Director vs. Rating', 'Director', 'Rating')
plot_fig(runtime, rating, 'Runtime vs. Rating', 'Runtime', 'Rating')

plt.show()

