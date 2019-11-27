import pandas as pd
import sys
import re

#SCHEMA
#title, genre, year(int), decade, runtime (minutes, int), rating (out of 10, float to 1 decimal place), director, actor1, actor2, actor3, gross (millions, float to 2 decimals places)

schema = ['title', 'genre', 'year', 'runtime', 'rating', 'director','actor1', 'actor2', 'actor3']
schema_with_gross = ['title', 'genre', 'year', 'runtime', 'rating', 'director','actor1', 'actor2', 'actor3', 'gross']


#for stripping "minutes" and just extracting numbers from runtime column, used in rotten tomatoes df
input_pattern = re.compile(r'(\d+)')
def get_runtime(runtime):
    match = input_pattern.search(runtime)
    if match:
        return match.group(1)
    else:
        return None


def clean_imdb(df):

    #split list of 4 actors into separate columns and strip commas
    df[['actor1', 'actor2', 'actor3', 'actor4']] = df.Actors.str.split(',', expand=True)
    #include only 3 actors
    df = df.drop(['Actors', 'actor4'], axis = 1)
    df.columns = df.columns.str.lower()
    #rename columns for consistency
    df = df.rename(columns = {'runtime (minutes)': 'runtime', 'revenue (millions)': 'gross'})
    #reorder columns
    df = df[schema_with_gross]
    #drop na values
    df = df.dropna()

    return df


def clean_metadata(df):

    #rename columns
    df = df.rename(columns = {'movie_title': 'title', 'genres': 'genre', 'title_year': 'year', 'duration':'runtime', 'imdb_score':'rating', 'director_name':'director', 'actor_1_name':'actor1', 'actor_2_name':'actor2', 'actor_3_name':'actor3'})
    #convert gross into millions 
    df['gross'] = (df['gross']/1000000).round(2)
    #drop na values
    df = df.dropna()
    #make sure numbers are ints
    df = df.astype({'year': 'int32','runtime':'int32'})
    #reformat genre so its a comma separated list like IMDB genre list
    df['genre'] = df['genre'].str.replace('|',',')
    #reorder columns
    df = df[schema_with_gross]
    
    return df






def clean_movies(df):

    #rename columns
    df = df.rename(columns = {'thtr_rel_year': 'year', 'imdb_rating': 'rating'})
    #convert genre into comma separated list
    df['genre'] = df['genre'].str.replace('&',',')
    df['genre'] = df['genre'].str.replace(' ', '')
    #drop na
    df = df.dropna()
    #convert to into
    df = df.astype({'year': 'int32', 'runtime':'int32'})
    #include only 3 actors
    df = df.drop(['actor4', 'actor5'], axis = 1)
    df = df[schema]

    return df


def clean_rotten(df):

    #rename columns
    df.columns = df.columns.str.lower()
    df = df.rename(columns = {'director 1': 'director', 'cast 1': 'actor1', 'cast 2': 'actor2', 'cast 3': 'actor3'})
    #drop na
    df = df.dropna()
    #extract runtime number, dropping the word "minutes"
    df['runtime'] = df['runtime'].apply(get_runtime)
    #reorder columns
    df = df[['title', 'genre', 'year', 'runtime', 'director','actor1', 'actor2', 'actor3']]

    return df


def clean_rott_ratings(df):

    #rename columns
    df.columns = df.columns.str.lower()
    df = df.rename(columns = {'movie': 'title'})
    #convert rating to 10 point scale
    df['rating'] = df['rating']/10

    return df


def join_ratings(rotten, ratings):
    df = pd.merge(rotten, ratings, on = 'title')
    df = df.groupby(['title', 'year', 'runtime', 'director', 'actor1', 'actor2', 'actor3', 'rating']).genre.unique().reset_index()
    df = df[schema]
    df['genre'] = df['genre'].apply(', '.join)

    return df


def combine(df1, df2, df3, df4):
    df = pd.concat([df1, df2, df3, df4], sort = False)
    #strip leading and trailing space on titles
    df['title'] = df['title'].str.strip()
    df = df.drop_duplicates(subset='title', keep='first')

    #add decade column, for use in analysis
    df['decade'] = (df['year']//10)*10

    # decades range from 1920-2010
    # decades = joined.groupby('decade').count()

    #since there are <40 sample points for 1920, 1930, 1940, 1950 and 1960, we grouped them all together into 1920-1960
    df['decade'] = df['decade'].apply(lambda y: y if y >=1970 else "1920-1960")

    df = df.sort_values(by=['title']).reset_index()
    df = df[['title', 'genre', 'year', 'decade','runtime', 'rating', 'director','actor1', 'actor2', 'actor3', 'gross']]

    return df



def main():

    #pull columns from each dataset that is common to all data sets
    imdb = pd.read_csv(sys.argv[1], usecols = ['Title','Genre', 'Year', 'Runtime (Minutes)', 'Rating', 'Director', 'Actors', 'Revenue (Millions)'])
    cleaned_imdb = clean_imdb(imdb)
    

    metadata = pd.read_csv(sys.argv[2], usecols = ['movie_title', 'genres', 'title_year', 'duration', 'imdb_score', 'director_name', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'gross'])
    cleaned_meta = clean_metadata(metadata)
    

    movie = pd.read_csv(sys.argv[3], usecols = ['title', 'genre', 'thtr_rel_year', 'runtime', 'imdb_rating', 'director', 'actor1', 'actor2', 'actor3', 'actor4', 'actor5'])
    cleaned_movies = clean_movies(movie)
    

    #rotten tomato scraped data for 25000 movies WITHOUT ratings
    rotten = pd.read_csv(sys.argv[4], usecols = ['Title', 'Genre', 'Year', 'Runtime', 'Director 1', 'Cast 1', 'Cast 2', 'Cast 3'])
    cleaned_rotten = clean_rotten(rotten)
  
    #rotten tomato ratings for ~200 movies
    rotten_ratings = pd.read_csv(sys.argv[5], sep = '\t', usecols = ['Movie', 'Rating'])
    cleaned_ratings = clean_rott_ratings(rotten_ratings)

    #join both rotten tomatoes datasets on common movie titles
    joined = join_ratings(cleaned_rotten, cleaned_ratings)
   
    final = combine(cleaned_imdb, cleaned_meta, cleaned_movies, joined)
    #print(final)
    final.to_csv('all.csv')
  


if __name__ == '__main__':
    main()