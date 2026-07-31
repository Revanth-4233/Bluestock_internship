# Befor data analysis we can perform data cleaning using df.shape, df.dtypes. df.head()
# df.shape ->  to check data is loaded correctly or not it shows no.of rows and columns
# df.dtypes ->  to check the column data types
# df.head() -> to see first 5 rows and if incase any null vales are there that fill with " NaN "


import pandas as pd

df = pd.read_csv('data/raw/10_benchmark_indices.csv')

print(df.shape)
print(df.dtypes)
print(df.head())
