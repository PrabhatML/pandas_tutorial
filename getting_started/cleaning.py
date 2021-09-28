import pandas as pd

df = pd.read_csv('getting_started/dirtydata.csv')

# print(df.to_string())

# Removing rows with NaN
# df.dropna(inplace=True)

# Removing cols with NaN
# df.dropna(inplace=True,axis=1)

# Fill NaN
df.fillna('2020/12/16',inplace=True)

print(df.to_string())
