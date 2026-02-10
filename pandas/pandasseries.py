# create a simple pandas series from a list
import pandas as pd
a=[1,7,2]
myvar=pd.Series(a)
print(myvar)
# return the first values of series
print("first values", myvar[0])
# with the index argument you can name you own labels
# create you own labels:
import pandas as pd
a=[1,7,2]
myvar=pd.Series(a, index=["x", "y" ,"z"])
print(myvar)
# when you have created labels , you can access an item by referring to the label
# Return the value of "y"
print(myvar["y"])
# you can also use a key/value object , like a dictionary , when creating a Series
# create a Simple Pandas Series from a dictionary
import pandas as pd
calories={"day1":420, "day2":380, "day3":390}
myvar=pd.Series(calories)
print(myvar)
# create a Series using only data from "day1" and "day2":
import pandas as pd
calories={"day1":420, "day2":380, "day3":390} 
myvar=pd.Series(calories, index=["day1","day2"])
print(myvar)
# dataframes
# Data sets in pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table
# create a DataFrame from two Series:
import pandas as pd
data={
    "calories":[420, 380, 390],
    "duration":[50,40,45]
    }
myvar=pd.DataFrame(data)
print(myvar)