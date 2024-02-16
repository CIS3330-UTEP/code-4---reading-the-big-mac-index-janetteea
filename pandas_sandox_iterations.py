# Lecture 2.14.24
# Refer to Lecture 2.12.24 for Code 4

# len(df) ---> 1631 rows x 19 columns
# len(df.columns) ---> number of columns

import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

# print (df)
# print (df.columns)
# print (type(df.columns))
# print (len(df.columns))

# print (len(df))
# print (df.index)
# print (len(df.index))
# print (type(df.index))

# numbers = range(1631)
# print (numbers)

# for i in df.index:
    # print (i)
    # print (df['dollar_price'][i])
    # print (df.loc[i]['name'])
    # print (df.iloc[i]['dollar_price'])
    # print (df.loc[i])
    # print (type(df.loc[i]))

# df_mex = df.query('iso_a3 == "MEX"')
# print (df_mex)

# for i in range(len(df)):
    # print (i)
    # print (df_mex.loc[df_mex.index[i]])

    # for index, row in df.iterrows():
    #     print (row)
    #     print (df['name'][index])

# Apply() in Pandas
        
def get_new_name(row):
    # print (row)
    new_column_value = f"{row['name']} ({row['iso_a3']})"
    # print (new_column_value)
    return new_column_value

# print (df.apply(get_new_name, axis=1))
# df['new_name'] = df.apply(get_new_name, axis=1)
# print (df)

result = df.apply(get_new_name, axis=1)
# return result...?
# print (type(result))...?