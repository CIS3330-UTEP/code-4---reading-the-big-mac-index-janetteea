# Lecture 2.12.24

# Series - arrays (lists) of a single data type (str, int, float)

# Index - data structure for identifying a row in a Series or a DataFrame;
# can be numeric or alpha numeric

import pandas as pd

# list_teams = ['49ers', 'KC', 'Cowboys', 'Steelers']

# print (type(list_teams))

# print (list_teams)

# series_teams = pd.Series(list_teams)

# print (series_teams)
# print (type(series_teams))

# students = {'New York': 'Janette', 'Ohio': 'David', 'Iowa': 'Justin', 'Colorado': 'Robert'}

# print (type(students))
# print (students)

# student_series = pd.Series(index=students.keys(),data=students.values())

# print(type(student_series))
# print (student_series)
# print (student_series.index)

# New Info

df = pd.read_csv('big-mac-full-index.csv')

# print(type(df))
# print (df.columns)
# print (type(df.columns)) #will print the names of individual columns

# print (df)
# print (df['name'])
# print (type(df['name']))

# For Code 4

country_code = ['USA', 'MEX']
query_text = f"iso_a3 == @country_code"

df_usa = df.query(query_text)
#print (df_usa)
#print (round(df_usa['local_price'].mean(),2))

idx_dollar_price = df_usa['dollar_price'].idxmin()
#print (idx_dollar_price)




