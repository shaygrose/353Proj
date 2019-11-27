import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import random
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier


data = pd.read_csv(sys.argv[1], index_col = 0)
# print(data.head())
# data.drop(columns = ['index'])

def random_genre(x):
    return random.choice(x.split(','))

data['genre_one'] = data['genre'].apply(random_genre)

directors_names = data['director'].unique()
actor_1_name = data['actor1'].unique()
actor_2_name = data['actor2'].unique()
actor_3_name = data['actor3'].unique()
genre_genre = data['genre'].unique()
decade_code = data['decade'].unique()
genre_codecode = data['genre_one'].unique()

def get_director_index(x, leest):
    #print(np.where(directors_names == x))
    return np.where(leest == x)[0][0]



data['director code'] = data['director'].apply(get_director_index, leest = directors_names)
data['actor1_code'] = data['actor1'].apply(get_director_index, leest = actor_1_name)
data['actor2_code'] = data['actor2'].apply(get_director_index, leest = actor_2_name)
data['actor3_code'] = data['actor3'].apply(get_director_index, leest = actor_3_name)
data['genre_code'] = data['genre'].apply(get_director_index, leest = genre_genre)
data['decade_code'] = data['decade'].apply(get_director_index, leest = decade_code)
data['genre_one_code'] = data['genre_one'].apply(get_director_index, leest = genre_codecode)


#converting runtime to hours and rounding to nearest decimal place
data['runtime'] = (data['runtime']/60).round(1)
# print(data['runtime'].head())

#print(data.head())
#data.to_csv('text2.csv')

def score_polyfit(n):
    model = make_pipeline(
        PolynomialFeatures(degree = n, include_bias = True),
        LinearRegression(fit_intercept = False)
    )
    model.fit(X_train, y_train)
    print('n=%i: score=%.5g' % (n, model.score(X_valid, y_valid)))

X = data[['director code', 'runtime', 'genre_code', 'decade_code']]
X_2 = data[['director code', 'runtime','genre_one_code', 'decade_code']]
#round each rating to the nearest whole number
y = data['rating'].round(0)
X_train, X_valid, y_train, y_valid = train_test_split(X,y,test_size = 0.33, random_state=42)
X_train_2, X_valid_2, y_train_2, y_valid_2 = train_test_split(X_2,y,test_size = 0.33, random_state=42)

rand_forest_model = make_pipeline(
        RandomForestClassifier(n_estimators=100,
        max_depth=8, min_samples_leaf=10)
    )

voting_model = make_pipeline(
    StandardScaler(),
    VotingClassifier([
    ('nb', GaussianNB()),
    ('knn', KNeighborsClassifier(10)),
    ('svm', SVC(kernel='linear', C=2.0)),
    ('tree1', DecisionTreeClassifier(max_depth=10)),
    ('tree2', DecisionTreeClassifier(min_samples_leaf=10)),
    ('tree3', RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_leaf=10)),
    ])
)

Boosting_model = GradientBoostingClassifier(n_estimators = 100, max_depth = 3, min_samples_leaf = 5)


Neural_model = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(2,2), activation='logistic')



rand_forest_model.fit(X_train, y_train)
print(rand_forest_model.score(X_valid, y_valid)) # 0.42461340206185566

voting_model.fit(X_train, y_train)
print(voting_model.score(X_valid, y_valid)) # 0.3943298969072165

Boosting_model.fit(X_train, y_train)
print(Boosting_model.score(X_valid, y_valid)) # 0.4220360824742268

Neural_model.fit(X_train, y_train)
print(Neural_model.score(X_valid, y_valid)) # 0.33698453608247425

print('  ')
print('with random_genre')
print('   ')

rand_forest_model.fit(X_train_2, y_train_2)
print(rand_forest_model.score(X_valid_2, y_valid_2)) # 0.41365979381443296

voting_model.fit(X_train_2, y_train_2)
print(voting_model.score(X_valid_2, y_valid_2)) # 0.4117268041237113

Boosting_model.fit(X_train_2, y_train_2)
print(Boosting_model.score(X_valid_2, y_valid_2)) # 0.41301546391752575

Neural_model.fit(X_train_2, y_train_2)
print(Neural_model.score(X_valid_2, y_valid_2)) # 0.3389175257731959

#sdlkfasklf

#score for just director and genre
#0.389819587628866

#score for director, runtime and genre
#0.40850515463917525

# score_polyfit(1)
# score_polyfit(5)
# score_polyfit(9)
# score_polyfit(13)
# score_polyfit(17)

# for just director and genre
# n=1: score=0.0039917
# n=5: score=-1.0558
# n=9: score=-2830.2
# n=13: score=-5995.4
# n=17: score=-27.439
