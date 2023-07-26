import pandas as pd
import numpy as np

exam_data = {
    'name': ['Анастасия', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'оценка': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'попытки': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'уточнять': ['да', 'нет', 'да', 'нет', 'нет', 'да', 'да', 'нет', 'нет', 'да']}
indexes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=indexes)
print(df)
print(df.loc[['a', 'd', 'f', 'j']][['оценка', 'попытки']])
print(f'Кол-во строк - {df.shape[0]}, кол-во столбцов - {df.shape[1]}')
print(df[df['оценка'].isnull()])
print(df[(df['оценка'] > 15) & (df['попытки'] < 2)])
df.loc['d', 'оценка'] = 11.5
print(df)
print(df.groupby('name').agg({'попытки': 'sum'}))
print(np.sum(df['попытки']))
print(df['оценка'].mean())

df.loc['k'] = ['Nikita', 100, '1', 'да']
print(df)
df = df.drop('k')
print(df)

print(df.sort_values('name', ascending=False))
print(df.sort_values('оценка'))

df['уточнять'] = df['уточнять'].map({'да': 'Истина', 'нет': 'Ложь'})
print(df)
df['name'] = df['name'].replace('James', 'Suresh')
print(df)
del df['попытки']
df['IQ'] = [100, 90, 120, 130, 120, 100, 80, 90, 150, 100]
print(df)

for index, row in df.iterrows():
    print(row['name'])
print(df.columns)

df = df.rename(columns={'уточнять': 'Verify', 'оценка': 'Score', 'попытки': 'Attempts', 'name' : 'Name'})
print(df)


df = df[['Name', 'IQ', 'Score', 'Verify']]
print(df)

df.loc['k'] = ['Nikita', 150, 50, 'Истина']
print(df)

print(df.info())


