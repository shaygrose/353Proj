import pandas as pd
import sys
import re

# SCHEMA
#title, genre, year(int), decade, runtime (minutes, int), rating (out of 10, float to 1 decimal place), director, actor1, actor2, actor3, gross (millions, float to 2 decimals places)



#for stripping "minutes" and just extracting numbers from runtime column, used in rotten tomatoes df
input_pattern = re.compile(r'(\d+)')
def get_runtime(runtime):
    match = input_pattern.search(runtime)
    if match:
        return match.group(1)
    else:
        return None


#IMDB
imdb = pd.read_csv(sys.argv[1], usecols = ['Title','Genre', 'Year', 'Runtime (Minutes)', 'Rating', 'Director', 'Actors', 'Revenue (Millions)'])
#reorder columns
imdb[['actor1', 'actor2', 'actor3', 'actor4']] = imdb.Actors.str.split(',', expand=True)
#include only 3 actors
imdb = imdb.drop(['Actors', 'actor4'], axis = 1)
imdb = imdb[['Title','Genre', 'Year', 'Runtime (Minutes)', 'Rating', 'Director', 'actor1', 'actor2', 'actor3', 'Revenue (Millions)']]
imdb.columns = imdb.columns.str.lower()
#rename columns for consistency
imdb = imdb.rename(columns = {'runtime (minutes)': 'runtime', 'revenue (millions)': 'gross'})
imdb = imdb.dropna()




#MOVIES METADATA
metadata = pd.read_csv(sys.argv[2], usecols = ['movie_title', 'genres', 'title_year', 'duration', 'imdb_score', 'director_name', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'gross'])
#reorders columns
metadata = metadata[['movie_title', 'genres', 'title_year', 'duration', 'imdb_score', 'director_name', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'gross']]
#rename columns
metadata = metadata.rename(columns = {'movie_title': 'title', 'genres': 'genre', 'title_year': 'year', 'duration':'runtime', 'imdb_score':'rating', 'director_name':'director', 'actor_1_name':'actor1', 'actor_2_name':'actor2', 'actor_3_name':'actor3'})
metadata = metadata.dropna()
metadata['gross'] = (metadata['gross']/1000000).round(2)
metadata = metadata.astype({'year': 'int32','runtime':'int32'})
#reformat genre so its a comma separated list like IMDB genre list
metadata['genre'] = metadata['genre'].str.replace('|',',')





# MOVIES
movie = pd.read_csv(sys.argv[3], usecols = ['title', 'genre', 'thtr_rel_year', 'runtime', 'imdb_rating', 'director', 'actor1', 'actor2', 'actor3', 'actor4', 'actor5'])
#reorder columns
movie = movie[['title', 'genre', 'thtr_rel_year', 'runtime', 'imdb_rating', 'director', 'actor1', 'actor2', 'actor3', 'actor4', 'actor5']]
#rename columns
movie = movie.rename(columns = {'thtr_rel_year': 'year', 'imdb_rating': 'rating'})
movie = movie.dropna()
movie = movie.astype({'year': 'int32', 'runtime':'int32'})
#include only 3 actors
movie = movie.drop(['actor4', 'actor5'], axis = 1)




# ROTTEN TOMATOES (no ratings)
rotten = pd.read_csv(sys.argv[4], usecols = ['Title', 'Genre', 'Year', 'Runtime', 'Director 1', 'Cast 1', 'Cast 2', 'Cast 3', 'Cast 4', 'Cast 5', 'Cast 6'])
#reorder columns
rotten = rotten[['Title', 'Genre', 'Year', 'Runtime', 'Director 1', 'Cast 1', 'Cast 2', 'Cast 3', 'Cast 4', 'Cast 5', 'Cast 6']]
#rename columns
rotten.columns = rotten.columns.str.lower()
rotten = rotten.rename(columns = {'director 1': 'director', 'cast 1': 'actor1', 'cast 2': 'actor2', 'cast 3': 'actor3', 'cast 4': 'actor4', 'cast 5': 'actor5', 'cast 6': 'actor6'})
rotten = rotten.dropna()
#extract runtime number
rotten['runtime'] = rotten['runtime'].apply(get_runtime)
#include only 3 actors
rotten = rotten.drop(['actor4', 'actor5', 'actor6'], axis = 1)

# ROTTEN TOMATOES (has ratings)

rotten_ratings = pd.read_csv(sys.argv[5], sep = '\t', usecols = ['Movie', 'Rating'])
rotten_ratings.columns = rotten_ratings.columns.str.lower()
rotten_ratings = rotten_ratings.rename(columns = {'movie': 'title'})
rotten_ratings['rating'] = rotten_ratings['rating']/10

# combine rotten tomatoes datasets on common movies, to get ratings for movies
both_rotten = pd.merge(rotten, rotten_ratings, on = 'title')
both_rotten = both_rotten.groupby(['title', 'year', 'runtime', 'director', 'actor1', 'actor2', 'actor3', 'rating']).genre.unique().reset_index()
both_rotten = both_rotten[['title', 'genre', 'year', 'runtime',  'rating', 'director', 'actor1', 'actor2', 'actor3']]
both_rotten['genre'] = both_rotten['genre'].apply(', '.join)


#FINAL
#concat all datasets together into one dataframe
joined = pd.concat([imdb, metadata, movie, both_rotten], sort=False)
joined['title'] = joined['title'].str.strip()

#drop duplicate movies
joined = joined.drop_duplicates(subset='title', keep='first')

#add decade column
joined['decade'] = (joined['year']//10)*10

# decades range from 1920-2010
# decades = joined.groupby('decade').count()
# print(decades['title'])

#since there are <40 sample points for 1920, 1930, 1940, 1950 and 1960, we grouped them all together into 1920-1960
joined['decade'] = joined['decade'].apply(lambda y: y if y >=1970 else "1920-1960")
joined['genre'] = joined['genre'].str.replace('&',',')
joined['genre'] = joined['genre'].str.replace(' ', '')

#reorder columns
joined = joined[['title', 'genre', 'year', 'decade','runtime', 'rating', 'director', 'actor1', 'actor2', 'actor3', 'gross']]
joined = joined.sort_values(by=['title']).reset_index()
#print(joined)
#print(joined['title'].value_counts())
joined.to_csv('all.csv')
