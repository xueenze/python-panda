import pandas as pd
from datetime import datetime

movie_pd = pd.read_csv(
    '../data/douban_movie.csv', header=0, sep='\t')

movie_pd['release_date'] = pd.to_datetime(movie_pd['release_date'])
movie_pd['total_day'] = movie_pd['release_date'].map(
    lambda x: (datetime.now() - x).total_seconds() / (3600 * 24))
movie_pd['daily_vote'] = movie_pd['vote_count'] / movie_pd['total_day']

print(movie_pd[['release_date', 'total_day', 'vote_count', 'daily_vote']].head())