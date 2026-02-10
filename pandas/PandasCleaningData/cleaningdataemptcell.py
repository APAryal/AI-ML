# pandas-Cleaning Empty cells
# Return a new data frame with no empty celss
import pandas as pd
df=pd.read_csv('data.csv')
new_df=df.dropna()
print(new_df.to_string())

# Remove all rows will Null values:
import pandas as pd
df=pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df.to_string())
# Replace Null values with the number 130:
import pandas as pd
df=pd.read_csv('data.csv')
df.fillna(130, inplace=True)
print(df.to_string())
# Replace Null values in the "calories" with the number 130:
print("replace null values in the 'calories' with the number 130:")
import pandas as pd
df=pd.read_csv('data.csv')
df.fillna({"Calories":130},inplace=True)
print(df.to_string())

# calculate the Mean , and replace any empty values with it
import pandas as pd
df=pd.read_csv('data.csv')
x=df["Calories"].mean()
df.fillna({"Calories":x}, inplace=True)
print(df.to_string())
# Calculate the Median , and replace any empty values with it:
import pandas as pd
df=pd.read_csv("data.csv")
x=df["Calories"].median()
df.fillna({"Calories":x}, inplace=True)
print(df.to_string())

# Calculate the Mode and replacce any empty values with it
import pandas as pd
df=pd.read_csv('data.csv')
x=df["Calories"].mode()[0]
df.fillna({"Calories":x},inplace=True)
print(df.to_string())