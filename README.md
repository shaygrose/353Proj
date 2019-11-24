# 353Proj
Movie Rating Analysis

Using IMDb and Rotten Tomatoes datasets to find out characteristics of movies which are succesful at the box office.

To run data prep:
python3 data_prep.py IMDB.csv metadata.csv movies.csv rotten.csv rotten-rating.csv
Outputs one aggregated csv called all.csv

To run dataplot:
python3 dataplot.py all.csv
outputs 4 .png plots

to run ML.py:
python3 ML.py all.csv
