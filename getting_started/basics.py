import pandas as pd


# print(dir(pd))

# dataset = {
#     'cars' : ['BWM','Volvo',"Ford"],
#     'passings' : [3,7,8]
# }

# df = pd.DataFrame(dataset)

# print(df)
# print(df.loc[0])

# df = pd.DataFrame(dataset,index=['E1','E2','E3'])


# print(df)
# print(df.loc[['E1']])


# df = pd.read_csv('getting_started/data.csv')
# print(df)
# print(df.to_string())
# print(df.to_html())
# print(df.to_dict())
# print(df.to_json())


# df = pd.read_json('getting_started/data.json')


df = pd.read_csv('getting_started/data.csv')
print(df.head(10))
print(df.tail(10))

print(df.info())
















# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)
# print(myvar)