import pandas as pd

movie_pd = pd.read_csv(
    '../data/douban_movie.csv', header=0, sep='\t')

movie_level_list = list()

for i in movie_pd.index:
    score = movie_pd.loc[i, 'score']
    if score < 7.5:
        movie_level = '8'
    elif 7.5 <= score < 9.0:
        movie_level = 'A'
    else:
        movie_level = 'S'
    movie_level_list.append(movie_level)

movie_pd['movie_level'] = pd.Series(movie_level_list)
print((movie_pd[['score', 'movie_level']]).head())
    