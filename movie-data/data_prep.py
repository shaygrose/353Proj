import pandas as pd
import sys
import re

# SCHEMA
#runtime (minutes, int), rating(out of 10, float to 1 decimal place), gross (millions, float to 2 decimals places), year (int)



#for stripping "minutes" and just extracting numbers from runtime column, used in rotten tomatoes df
input_pattern = re.compile(r'(\d+)')
def get_runtime(runtime):
    match = input_pattern.search(runtime)
    if match:
        return match.group(1)
    else:
        return None


#IMDB
# has all actors in single column as list
# has genres as list separated by comma (ex. Action,Adventure,Fantasy)
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
#also need to decide if we want to have actors as one columns with a list of *3 actors*, or 3 separate columns with one actor each
#has list of genres separated with | (ex. Action|Adventure|Fantasy)
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
#doesn't have box office gross
#*5 actors*
#one genre
movie = pd.read_csv(sys.argv[3], usecols = ['title', 'genre', 'thtr_rel_year', 'runtime', 'imdb_rating', 'director', 'actor1', 'actor2', 'actor3', 'actor4', 'actor5'])
#reorder columns
movie = movie[['title', 'genre', 'thtr_rel_year', 'runtime', 'imdb_rating', 'director', 'actor1', 'actor2', 'actor3', 'actor4', 'actor5']]
#rename columns
movie = movie.rename(columns = {'thtr_rel_year': 'year', 'imdb_rating': 'rating'})
movie = movie.dropna()
movie = movie.astype({'year': 'int32', 'runtime':'int32'})
#include only 3 actors
movie = movie.drop(['actor4', 'actor5'], axis = 1)


rotten_ratings = pd.read_csv(sys.argv[5], sep = '\t', usecols = ['Movie', 'Rating'])
rotten_ratings.columns = rotten_ratings.columns.str.lower()
rotten_ratings = rotten_ratings.rename(columns = {'movie': 'title'})
rotten_ratings['rating'] = rotten_ratings['rating']/10
#print(rotten_ratings.head())

# ROTTEN TOMATOES 
#doesn't have much useful data, but could possibly join it to one of the other dataframes on common movie titles
#*6 actors*
#one genre
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





both_rotten = pd.merge(rotten, rotten_ratings, on = 'title')

both_rotten = both_rotten.groupby(['title', 'year', 'runtime', 'director', 'actor1', 'actor2', 'actor3', 'rating']).genre.unique().reset_index()

both_rotten = both_rotten[['title', 'genre', 'year', 'runtime',  'rating', 'director', 'actor1', 'actor2', 'actor3']]
both_rotten['genre'] = both_rotten['genre'].apply(', '.join)




joined = pd.concat([imdb, metadata, movie, both_rotten], sort=False)
joined['title'] = joined['title'].str.strip()

joined = joined.drop_duplicates(subset='title', keep='first')
#print(joined)

input_pattern_2 = re.compile(r'\d\d(\d)\d')
def get_decade(year):
    match = input_pattern_2.search(year)
    if match:
        return match.group(1)
    else:
        return None

joined['decade'] = (joined['year']//10)*10

joined = joined[['title', 'genre', 'year', 'decade','runtime',  'rating', 'director', 'actor1', 'actor2', 'actor3']]


joined = joined.sort_values(by=['title'])

#print(joined['title'].value_counts())
joined.to_csv('all.csv')


