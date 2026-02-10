# create a simple pandas DataFrame
import pandas as pd
data={
    "calories":[420, 380, 390],
    "duration":[50, 40,45]
}
df=pd.DataFrame(data)
print(df)
# return row 0
# refer to the row index
print(df.loc[0])
# return row 0 and 1
print(df.loc[[0,1]])
# named indexes
# with the index argument, you can name your own indexes
# Add a list of names to give each row a name:
import pandas as pd
data={
    "calories":[420, 380, 390],
    "duration":[50,40,45]
}
df=pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)
# Return "day2"
print(df.loc["day2"])
# load a comma separated file (csv file) into a DataFrame
import pandas as pd
df=pd.read_csv('data.csv')
print(df)