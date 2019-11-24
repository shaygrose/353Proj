import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.color import lab2rgb
from skimage.color import rgb2lab
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


data = pd.read_csv(sys.argv[1], index_col = 0)
data.drop(columns = ['index'])

directors_names = data['director'].unique()
actor_1_name = data['actor1'].unique()
actor_2_name = data['actor2'].unique()
actor_3_name = data['actor3'].unique()


data['director code'] = data['director'].astype('category', CatergoricalDtype = directors_names).cat.codes
data['actor1_code'] = data['actor1'].astype('category', CatergoricalDtype = actor_1_name).cat.codes
data['actor2_code'] = data['actor2'].astype('category', CatergoricalDtype = actor_2_name).cat.codes
data['actor3_code'] = data['actor3'].astype('category', CatergoricalDtype = actor_3_name).cat.codes

print(data['genre'][0][0])
