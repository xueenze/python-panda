import pandas as pd

movie_pd = pd.read_csv(
    '../data/douban_movie.csv', header = 0, sep = '\t')

print(movie_pd.head())
print(movie_pd.tail())
# print(movie_pd.info())