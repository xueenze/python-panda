import pandas as pd

temp_dict = {
    'score': [8.9, 8.2, 9.3],
    'category': ['悬疑', '动作', '爱情']
}

temp_pd = pd.DataFrame(temp_dict)
print(temp_pd)