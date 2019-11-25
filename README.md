# 353 Project
Movie Rating Analysis

IMDb and Rotten Tomatoes datasets used to find characteristics of movies which are succesful at the box office.

**To run data prep:**
```
python3 data_prep.py IMDB.csv metadata.csv movies.csv rotten.csv rotten-rating.csv
```
Output: one aggregated csv called *all.csv*


**To run dataplot:**
```
python3 dataplot.py all.csv
```
Output: four '.png' plots


**To run ML.py:**
```
python3 ML.py all.csv
```
