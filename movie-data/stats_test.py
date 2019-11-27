import pandas as pd
import sys
from scipy import stats
import matplotlib.pyplot as plt


data = pd.read_csv(sys.argv[1])

correlate = data.corr(method = 'pearson')
print(correlate)
#contingency = [data['']]

print('rating normal test ',stats.normaltest(data['rating']).pvalue)
print('runtime normal test ',stats.normaltest(data['runtime']).pvalue)
print('runtime and levene ',stats.levene(data['rating'], data['runtime']).pvalue)


decade_1920_1960 = data[data['decade'] == '1920-1960']
decade_1970 = data[data['decade'] == '1970']
decade_1980 = data[data['decade'] == '1980']
decade_1990 = data[data['decade'] == '1990']
decade_2000 = data[data['decade'] == '2000']
decade_2010 = data[data['decade'] == '2010']

deckade = []
deckade.append(stats.mannwhitneyu(decade_1920_1960['rating'], decade_1970['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1970['rating'], decade_1980['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1980['rating'], decade_1990['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1990['rating'], decade_2000['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_2000['rating'], decade_2010['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1920_1960['rating'], decade_1980['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1920_1960['rating'], decade_1990['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1920_1960['rating'], decade_2000['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1920_1960['rating'], decade_2010['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1970['rating'], decade_1990['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1970['rating'], decade_2000['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1970['rating'], decade_2010['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1980['rating'], decade_2000['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1980['rating'], decade_2010['rating']).pvalue)
deckade.append(stats.mannwhitneyu(decade_1990['rating'], decade_2010['rating']).pvalue)

# for i in range(len(deckade)):
#     if deckade[i] < 0.05:
#         print(i)

print("pairs tend to sort higher than the other")
print("(1920-1960) - 1970")
print("1970 - 1980")
print("(1920-1960) - 1980")
print("(1920-1960) - 1990")
print("(1920-1960) - 2000")
print("(1920-1960) - 2010")
print("1970 - 1990")
print("1970 - 2000")
print("1970 - 2010")
print("1980 - 2000")
print("1980 - 2010")
