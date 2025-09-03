import pandas as pd

#read a csv file
sales = pd.read_csv('csv_file.csv')

#search w filter
search = dataframe[condition]
results = all_data[(all_data.column1 > all_data.column2) & (all_data.column3 > all_data.column4)]

#merge dataframes
merge_two_df = pd.merge(df1, df2)
merge_three_df = df1.merge(df2).merge(df3)
merge_two_w_rename = pd.merge(df1, df2.rename(columns={'old column': 'new column'}))
merge_two_w_suffixes = pd.merge(orders, products, left_on='product_id', right_on ='id', suffixes=['_orders', '_products'])
merge_w_outer = pd.merge(df1,df2, how='outer' or 'left' or 'right')

#concatenate dataframes
conc = pd.concat([df1, df2])
