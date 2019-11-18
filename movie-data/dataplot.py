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

def getGenreAndRating(data, genreColumn, genreRating, title, rating, genre):
    temp = pd.DataFrame()
    temp[genreColumn] = data[title][data[genre].str.contains(genreColumn)]
    temp[genreRating] = data[rating][data[genre].str.contains(genreColumn)]
    return temp

action = pd.DataFrame()
adventure = pd.DataFrame()
comedy = pd.DataFrame()
crime = pd.DataFrame()
scifi = pd.DataFrame()
drama = pd.DataFrame()
horror = pd.DataFrame()
romance = pd.DataFrame()
mystery = pd.DataFrame()

action[['Action', 'ActionRating']] = getGenreAndRating(data, 'Action', 'ActionRating', 'title', 'rating', 'genre')
adventure[['Adventure', 'AdventureRating']] = getGenreAndRating(data, 'Adventure', 'AdventureRating', 'title', 'rating', 'genre')
comedy[['Comedy', 'ComedyRating']] = getGenreAndRating(data, 'Comedy', 'ComedyRating', 'title', 'rating', 'genre')
crime[['Crime', 'CrimeRating']] = getGenreAndRating(data, 'Crime', 'CrimeRating', 'title', 'rating', 'genre')
scifi[['Sci-Fi', 'SciFiRating']] = getGenreAndRating(data, 'Sci-Fi', 'SciFiRating', 'title', 'rating', 'genre')
drama[['Drama', 'DramaRating']] = getGenreAndRating(data, 'Drama', 'DramaRating', 'title', 'rating', 'genre')
horror[['Horror', 'HorrorRating']] = getGenreAndRating(data, 'Horror', 'HorrorRating', 'title', 'rating', 'genre')
romance[['Romance', 'RomanceRating']] = getGenreAndRating(data, 'Romance', 'RomanceRating', 'title', 'rating', 'genre')




# plot_fig(title, rating, 'Title vs. Rating', 'Title', 'Rating')
# plot_fig(director, rating, 'Director vs. Rating', 'Director', 'Rating')
# plot_fig(runtime, rating, 'Runtime vs. Rating', 'Runtime', 'Rating')

# plt.show()

