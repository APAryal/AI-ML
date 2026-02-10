import pandas as pd
df=pd.read_csv('data.csv')

print(df.head())
print(df.tail())
print(df.shape)
print(df['city'])
print(df['name'])
print(df[df['age']<25])
print(df.describe())

