import pandas as pd

movie_pd = pd.read_csv(
    '../data/douban_movie.csv', header=0, sep='\t')

movie_pd['want_watch'] = movie_pd['score'].map(
    lambda x: 1 if x >= 9.0 else 0)

print(movie_pd.head())