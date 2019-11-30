# Movie Rating Analysis

With this project we took five datasets containing various attributes of movies (genre, year, runtime, director, actors etc), and their ratings, and tried to discover if certain characteristics influence how a movie is rated.

**Required Libraries**
- seaborn 
- sci-kitlearn  
- numpy  
- pandas  
- matplotlib  
- scipy  
- re  
- pylab  
- random  
- sys  



**Data Preparation**

First we took all the different data sets and extracted common features and converted them into the same units of measure (minutes for the runtime of movies etc.)

**To run data prep:**
```
python3 data_prep.py IMDB.csv metadata.csv movies.csv rotten.csv rotten-rating.csv
```
Outputs: one aggregated csv called *all.csv*

**Plotting**

Then we did a bunch of different graphical plots to see what influences movie ratings (director vs. rating etc.)

**To run dataplot:**
```
python3 dataplot.py all.csv
```
Outputs: four '.png' plots

**Predicting Movie Ratings**

Finally, we used a few different machine learning methods to try and predict the rating a movie receives based on its attributes. The best we did was around 42% accuracy using a Random Forest Classifier.

**To run ML.py:**
```
python3 ML.py all.csv
```

**Authors:**  
shaygrose: Shayna Grose  
pna18/patricksnotstar: Patrick Nguyen  
kchangch: Kidjou Argenis Chang (Big Sus)  
