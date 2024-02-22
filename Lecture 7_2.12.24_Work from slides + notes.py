import pandas as pd

# fruits = ['apple', 'melon', 'grapes', 'orange', 'kiwi']
# fruit_series = pd.Series(fruits)
# print (fruit_series)
# print (fruit_series.index)
# print (fruit_series.index.values)

# students = {"Texas": "Jazmin", "Alabama": "Roberto", "Virginia": "David", "California": "Alex"}
# student_series = pd.Series(data=students.values(), index=students.keys())

# print (student_series)
# print (student_series.index)

### FOR CODE 4 ###

filename = "./big-mac-full-index.csv"
df = pd.read_csv(filename)

#print (df) # prints the full dataframe for big mac file
#print (df.columns) # prints the names of all the columns in big mac file
#print (df['dollar_price']) # prints index position all values in dollar_price column

query = f"(iso_a3 == 'MEX')"
mxn_df = df.query(query)
min_idx = mxn_df['dollar_price'].idxmin()
max_idx = mxn_df['dollar_price'].idxmax()

#print (mxn_df['dollar_price']) # prints index position of all values in dollar_price within iso_a3 ---> MEX
#print (round(mxn_df['dollar_price'],2)) # prints same as above but rounded to 2 decimal places
#print(mxn_df['dollar_price'].median()) # prints out the median dollar price within iso_a3 ---> MEX
#print(round(mxn_df['dollar_price'].mean(),2)) # prints the avg value of dollar price within 
                                              # iso_a3 ---> MEX, rounding amount to 2 decimal places
## MINIMUMS ##
#print(min_idx) # prints index position of the minimum value
#print(mxn_df['dollar_price'].min()) # prints the minimum value of dollar price within iso_a3 ---> MEX
                                    # does the same thing as (mxn_df.loc[min_idx]['dollar_price'])
#print(mxn_df.loc[min_idx]) # prints out the entire row that has the minimum value (column header and value)
#print(mxn_df.loc[min_idx]['dollar_price']) # prints the minimum value of dollar price within iso_a3 ---> MEX
                                           # does the same thing as (mxn_df.['dollar_price'].min())

## MAXIMUMS ##
#print(max_idx) # prints index position of the maximum value
#print(mxn_df['dollar_price'].max()) # prints the maximum value of dollar price within iso_a3 ---> MEX
                                     # does the same thing as (mxn_df.loc[max_idx]['dollar_price'])
#print(mxn_df.loc[max_idx]) # prints out the entire row that has the maximum value (column header and value)
#print(mxn_df.loc[max_idx]['dollar_price']) # prints the maximum value of dollar price within iso_a3 ---> MEX
                                           # does the same thing as (mxn_df.['dollar_price'].max())

## FOR LOOP ##
#for index, row in mxn_df.iterrows():
    #print(index) # prints all the index positions of all rows within iso_a3 ---> MEX
    #print(row) # prints out all and entire row within iso_a3 ---> MEX (column header and value)


### INCORRECT CODE ###
# def get_the_cheapest_big_mac_price_by_year(year):
#     year_data = df.query("date == @year")
#     cheapest_index = year_data['dollar_price'].idxmin()
#     cheapest_row = year_data.loc[cheapest_index]

#     name = cheapest_row['name']
#     code = cheapest_row['iso_a3']
#     price = cheapest_row['dollar_price']
#     return f"{name} ({code}): ${price}"


















