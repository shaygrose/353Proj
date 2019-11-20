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
    x_axis = ax1.axes.get_xaxis().set_ticks([])
    # x_axis.set_visible(False)

def getGenreAndRating(data, genreColumn, title, rating, genre):
    temp = pd.DataFrame()
    temp[genreColumn] = data[title][data[genre].str.contains(genreColumn)]
    temp['Rating'] = data[rating][data[genre].str.contains(genreColumn)]
    return temp

action = pd.DataFrame()
adventure = pd.DataFrame()
biography = pd.DataFrame()
comedy = pd.DataFrame()
crime = pd.DataFrame()
drama = pd.DataFrame()
documentary = pd.DataFrame()
family = pd.DataFrame()
fantasy = pd.DataFrame()
history = pd.DataFrame()
horror = pd.DataFrame()
music = pd.DataFrame()
mystery = pd.DataFrame()
romance = pd.DataFrame()
scifi = pd.DataFrame()
thriller = pd.DataFrame()
war = pd.DataFrame()

action[['Title', 'Rating']] = getGenreAndRating(data, 'Action', 'title', 'rating', 'genre').reset_index(drop=True)
adventure[['Title', 'Rating']] = getGenreAndRating(data, 'Adventure', 'title', 'rating', 'genre').reset_index(drop=True)
biography[['Title', 'Rating']] = getGenreAndRating(data, 'Biography', 'title', 'rating', 'genre').reset_index(drop=True)
comedy[['Title', 'Rating']] = getGenreAndRating(data, 'Comedy', 'title', 'rating', 'genre').reset_index(drop=True)
crime[['Title', 'Rating']] = getGenreAndRating(data, 'Crime', 'title', 'rating', 'genre').reset_index(drop=True)
drama[['Title', 'Rating']] = getGenreAndRating(data, 'Drama', 'title', 'rating', 'genre').reset_index(drop=True)
documentary[['Title', 'Rating']] = getGenreAndRating(data, 'Documentary', 'title', 'rating', 'genre').reset_index(drop=True)
family[['Title', 'Rating']] = getGenreAndRating(data, 'Family', 'title', 'rating', 'genre').reset_index(drop=True)
fantasy[['Title', 'Rating']] = getGenreAndRating(data, 'Fantasy', 'title', 'rating', 'genre').reset_index(drop=True)
history[['Title', 'Rating']] = getGenreAndRating(data, 'History', 'title', 'rating', 'genre').reset_index(drop=True)
horror[['Title', 'Rating']] = getGenreAndRating(data, 'Horror', 'title', 'rating', 'genre').reset_index(drop=True)
music[['Title', 'Rating']] = getGenreAndRating(data, 'Music', 'title', 'rating', 'genre').reset_index(drop=True)
mystery[['Title', 'Rating']] = getGenreAndRating(data, 'Mystery', 'title', 'rating', 'genre').reset_index(drop=True)
romance[['Title', 'Rating']] = getGenreAndRating(data, 'Romance', 'title', 'rating', 'genre').reset_index(drop=True)
scifi[['Title', 'Rating']] = getGenreAndRating(data, 'Sci-Fi', 'title', 'rating', 'genre').reset_index(drop=True)
thriller[['Title', 'Rating']] = getGenreAndRating(data, 'Thriller', 'title', 'rating', 'genre').reset_index(drop=True)
war[['Title', 'Rating']] = getGenreAndRating(data, 'War', 'title', 'rating', 'genre').reset_index(drop=True)

averageRating = pd.DataFrame()
averageRating[['Action', 'Adventure', 'Biography', 'Comedy', 'Crime', 'Drama', 'Documentary', 'Family', 'Fantasy', 'History', 'Horror', 'Music',
                'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War']] = pd.concat([action['Rating'], 
                           adventure['Rating'], 
                           biography['Rating'],
                           comedy['Rating'],
                           crime['Rating'],
                           drama['Rating'], 
                           documentary['Rating'],
                           family['Rating'], 
                           fantasy['Rating'],
                           history['Rating'],
                           horror['Rating'],
                           music['Rating'],
                           mystery['Rating'],
                           romance['Rating'],
                           scifi['Rating'],
                           thriller['Rating'],
                           war['Rating']], axis=1, ignore_index=True)

# print(averageRating.mean())

plt.figure(figsize=(20,5))
averageRating.mean().plot.bar(rot=0)
plt.title('Average Rating by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Rating')


# plot_fig(title, rating, 'Title vs. Rating', 'Title', 'Rating')
# plot_fig(director, rating, 'Director vs. Rating', 'Director', 'Rating')
# plot_fig(runtime, rating, 'Runtime vs. Rating', 'Runtime', 'Rating')

plt.show()

