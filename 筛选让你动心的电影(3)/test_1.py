import pandas as pd

movie_pd = pd.read_csv(
    '../data/douban_movie.csv', header = 0, sep = '\t')

print(movie_pd.loc[0])

print(movie_pd['title'])