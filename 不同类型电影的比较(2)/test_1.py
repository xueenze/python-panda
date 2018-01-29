import pandas as pd
import numpy as np

movie_pd_1 = pd.read_csv(
    '../data/douban_movie.csv', header=0, sep='\t')

movie_pd_2 = pd.read_csv(
    '../data/douban_movie.csv', header=0, sep='\t')

merge_pd = pd.merge(movie_pd_1, movie_pd_2, on = 'movie_id')

print(merge_pd.head())
