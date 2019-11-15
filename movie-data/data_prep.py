import pandas as pd
import sys

IMDB = pd.read_csv(sys.argv[1])
metadata = pd.read_csv(sys.argv[2])
movie = pd.read_csv(sys.argv[3])
rotten = pd.read_csv(sys.argv[4])
