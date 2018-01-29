import pandas as pd

movie_pd = pd.read_csv(
    '../data/douban_movie.csv', header=0, sep='\t')

print(movie_pd.info())
print(movie_pd.describe())

print(movie_pd[['id', 'types']][1000:1006])

print(movie_pd[ movie_pd['id'] == 10455077 ][['types','category', 'rank']])

new_movie_pd = movie_pd.drop(['category', 'rank'], axis = 1)
new_movie_pd = new_movie_pd.drop_duplicates()

print(new_movie_pd.info())