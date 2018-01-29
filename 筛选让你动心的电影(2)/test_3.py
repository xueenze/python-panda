import pandas as pd

row1 = [8.9, '悬疑']
row2 = [8.2, '动作']
row3 = [9.3, '爱情']
row4 = [5.3, '恐怖']
temp_pd = pd.DataFrame(
    [ row1, row2, row3, row4 ], columns = ['score', 'category'])

print(len(temp_pd))
print(temp_pd.index)

temp_pd.index = ['movie_1', 'movie_2', 'movie_3', 'movie_4']
print(temp_pd.columns)

print(temp_pd)
