import pandas as pd
import sys


# has all actors in single columns as list
imdb = pd.read_csv(sys.argv[1], usecols = ['Title','Genre', 'Year', 'Runtime (Minutes)', 'Rating', 'Director', 'Actors', 'Revenue (Millions)'])
#reorder columns
imdb = imdb[['Title','Genre', 'Year', 'Runtime (Minutes)', 'Rating', 'Director', 'Actors', 'Revenue (Millions)']]
imdb.columns = imdb.columns.str.lower()
#rename columns for consistency
imdb = imdb.rename(columns = {'runtime (minutes)': 'runtime', 'revenue (millions)': 'gross'})


#need to convert meta data gross into millions (right now its just long number like 333,333,333)
#also need to decide if we want to have actors as one columns with a list of 3 actors, or 3 separate columns with one actor each
metadata = pd.read_csv(sys.argv[2], usecols = ['movie_title', 'genres', 'title_year', 'duration', 'imdb_score', 'director_name', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'gross'])
#reorders columns
metadata = metadata[['movie_title', 'genres', 'title_year', 'duration', 'imdb_score', 'director_name', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'gross']]
#rename columns
metadata = metadata.rename(columns = {'movie_title': 'title', 'genres': 'genre', 'title_year': 'year', 'duration':'runtime', 'imdb_score':'rating', 'director_name':'director', 'actor_1_name':'actor1', 'actor_2_name':'actor2', 'actor_3_name':'actor3'})


#doesn't have box office gross
movie = pd.read_csv(sys.argv[3], usecols = ['title', 'genre', 'thtr_rel_year', 'runtime', 'imdb_rating', 'director', 'actor1', 'actor2', 'actor3', 'actor4', 'actor5'])
#reorder columns
movie = movie[['title', 'genre', 'thtr_rel_year', 'runtime', 'imdb_rating', 'director', 'actor1', 'actor2', 'actor3', 'actor4', 'actor5']]
#rename columns
movie = movie.rename(columns = {'thtr_rel_year': 'year', 'imdb_rating': 'rating'})


#rotten tomatoes, doesn't have much useful data, but could possibly join it to one of the other dataframes on common movie titles
rotten = pd.read_csv(sys.argv[4], usecols = ['Title', 'Genre', 'Year', 'Runtime', 'Director 1', 'Cast 1', 'Cast 2', 'Cast 3', 'Cast 4', 'Cast 5', 'Cast 6'])
#reorder columns
rotten = rotten[['Title', 'Genre', 'Year', 'Runtime', 'Director 1', 'Cast 1', 'Cast 2', 'Cast 3', 'Cast 4', 'Cast 5', 'Cast 6']]
#rename columns
rotten.columns = rotten.columns.str.lower()
rotten = rotten.rename(columns = {'director 1': 'director', 'cast 1': 'actor1', 'cast 2': 'actor2', 'cast 3': 'actor3', 'cast 4': 'actor4', 'cast 5': 'actor5', 'cast 6': 'actor6'})

print(imdb.head())
print(metadata.head())
print(movie.head())
print(rotten.head())







