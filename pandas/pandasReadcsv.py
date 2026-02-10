# load the CSV into a DataFrame:
import pandas as pd
df=pd.read_csv('data1.csv')
print(df.to_string())

#print tha DataFrame without to_string() method:
import pandas as pd
df=pd.read_csv('data1.csv')
print(df)
# check the number of maximum returned rows
import pandas as pd
print(pd.options.display.max_rows)
# increase the maximum number of rows to display the entire DataFrame
import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data1.csv')

print(df)