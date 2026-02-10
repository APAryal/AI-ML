import pandas as pd
df=pd.read_csv('data.csv')

print(df.head())
print(df.tail())
print(df.shape)
print(df['city'])
print(df['name'])
print(df[df['age']<25])
print(df.describe())
# import pandas
import pandas
# now pandas is imported and ready to use
import pandas
mydataset={
    'cars':["BMW", "Volvo", "ford"],
    "passinfs":[3,7,2]
}
myvar=pandas.DataFrame(mydataset)
print(myvar)

# checking the pandas version 
# the version string is stored under _version_ attribute.
import pandas as pd
print(pd.__version__)