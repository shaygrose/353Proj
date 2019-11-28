import pandas as pd
import matplotlib.pyplot as plt
import sys
from scipy import stats
#import seaborn as sns
from pylab import *

data = pd.read_csv(sys.argv[1])
#sns.set()

title = data['title']
director = data['director']
genre = data['genre']
rating = data['rating']
year = data['year']
gross = data['gross']
runtime = data['runtime']

def getGenreAndRating(data, genreColumn):
    temp = pd.DataFrame()
    temp[genreColumn] = data['title'][data['genre'].str.contains(genreColumn)]
    temp['rating'] = data['rating'][data['genre'].str.contains(genreColumn)]
    temp['decade'] = data['decade'][data['genre'].str.contains(genreColumn)]
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

action[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Action').reset_index(drop=True)
adventure[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Adventure').reset_index(drop=True)
biography[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Biography').reset_index(drop=True)
comedy[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Comedy').reset_index(drop=True)
crime[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Crime').reset_index(drop=True)
drama[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Drama').reset_index(drop=True)
documentary[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Documentary').reset_index(drop=True)
family[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Family').reset_index(drop=True)
fantasy[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Fantasy').reset_index(drop=True)
history[['title', 'rating', 'decade']] = getGenreAndRating(data, 'History').reset_index(drop=True)
horror[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Horror').reset_index(drop=True)
music[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Music').reset_index(drop=True)
mystery[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Mystery').reset_index(drop=True)
romance[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Romance').reset_index(drop=True)
scifi[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Sci-Fi').reset_index(drop=True)
thriller[['title', 'rating', 'decade']] = getGenreAndRating(data, 'Thriller').reset_index(drop=True)
war[['title', 'rating', 'decade']] = getGenreAndRating(data, 'War').reset_index(drop=True)

averageRating = pd.DataFrame()
averageRating[['action', 'adventure', 'biography', 'comedy', 'crime', 'drama', 'documentary', 'family', 'fantasy', 'history', 'horror', 'music', 'mystery', 'romance', 'sci-Fi', 'thriller', 'war']] = pd.concat([action['rating'],
                                                                               adventure['rating'],
                                                                               biography['rating'],
                                                                               comedy['rating'],
                                                                               crime['rating'],
                                                                               drama['rating'],
                                                                               documentary['rating'],
                                                                               family['rating'],
                                                                               fantasy['rating'],
                                                                               history['rating'],
                                                                               horror['rating'],
                                                                               music['rating'],
                                                                               mystery['rating'],
                                                                               romance['rating'],
                                                                               scifi['rating'],
                                                                               thriller['rating'],
                                                                               war['rating']], axis=1, ignore_index=True)

# print(averageRating.mean())

#Plot Average rating vs. genre
plt.figure(figsize=(20,5))
averageRating.mean().plot.bar(rot=0)
plt.title('Average Rating by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Rating')
plt.savefig('Average Rating by Genre.png')

#decade rating
plt.figure(figsize=(20,5))
decade = data.groupby('decade').agg({'rating':'mean'})
decade.plot.bar(rot=0)
plt.xlabel('Decade')
plt.ylabel('Average Rating')
plt.title('Decade vs Average Rating')
plt.savefig('decade rating.png')


def getDirectorRating(d):
    avg_rating = data[data['director'] == d]['rating'].mean()
    return avg_rating

# director vs rating. Directors with at least 10 movies are considered
director_rating = pd.DataFrame()
director_rating[['director','count']] = data.groupby('director').size().reset_index()
director_rating = director_rating[director_rating['count'] >= 10].reset_index()
director_rating['rating'] = director_rating['director'].apply(getDirectorRating)
avg_rating = pd.DataFrame()
avg_rating[['director', 'rating']] = director_rating[['director', 'rating']]
avg_rating = avg_rating.sort_values(by = ['rating'], ascending = False)
fig = plt.figure(figsize=(15,10))
ax = plt.subplot()
ax.barh(avg_rating['director'], avg_rating['rating'])
ax.set_xlabel('Rating')
ax.set_ylabel('Director')
ax.set_title('Director vs Rating')
fig.savefig('director vs rating.png')

#runtime vs. rating
plt.figure(figsize=(15,5))
plt.title('Runtime vs Rating')
plt.ylabel('Rating')
plt.xlabel('Runtime (minutes)')
# (m,b) = polyfit(runtime, rating, 1)
# yp = polyval([m,b], runtime)
plt.plot(runtime, rating, '.b', alpha=0.5)
# plt.plot(runtime, yp, '-r', linewidth=2)

plt.savefig('runtime vs rating.png')
