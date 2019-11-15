import pandas as pd
import sys


imdb = pd.read_csv(sys.argv[1])
metadata = pd.read_csv(sys.argv[2])
movie = pd.read_csv(sys.argv[3])
rotten = pd.read_csv(sys.argv[4])

#COMMON FIELDS
#genre, director, year, length, title, rating (imdb_score, rating, imdb_rating,), actors (maybe top 3)

#only movie_metadata and IMDB have box office gross, movies has top200boxoffice boolean column, rotten tomatoes has nothing



#movie_metadata (3 actors listed)
#director_name,num_critic_for_reviews,duration,director_facebook_likes,actor_3_facebook_likes,actor_2_name,actor_1_facebook_likes,gross,genres,actor_1_name,movie_title,num_voted_users,cast_total_facebook_likes,actor_3_name,facenumber_in_poster,plot_keywords,movie_imdb_link,num_user_for_reviews,language,country,content_rating,budget,title_year,actor_2_facebook_likes,imdb_score,aspect_ratio,movie_facebook_likes

#movies (5 actors listed)
#title,title_type,genre,runtime,mpaa_rating,studio,thtr_rel_year,thtr_rel_month,thtr_rel_day,dvd_rel_year,dvd_rel_month,dvd_rel_day,imdb_rating,imdb_num_votes,critics_rating,critics_score,audience_rating,audience_score,best_pic_nom,best_pic_win,best_actor_win,best_actress_win,best_dir_win,top200_box,director,actor1,actor2,actor3,actor4,actor5,imdb_url,rt_url

#rotten tomatoes, doesn't have much useful data, but could possibly join it to one of the other dataframes on common movie titles
#has 6 actors listed
#Cast 1,Cast 2,Cast 3,Cast 4,Cast 5,Cast 6,Description,Director 1,Director 2,Director 3,Genre,Rating(pg-13 etc),Release Date,Runtime,Studio,Title,Writer 1,Writer 2,Writer 3,Writer 4,Year

#IMDB (actors field holds list of ~4 actors)
#Rank,Title,Genre,Description,Director,Actors,Year,Runtime (Minutes),Rating,Votes,Revenue (Millions),Metascore
