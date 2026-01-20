import pandas as pd

#loading dataset
df = pd.read_csv("datasets\Stock_Prices_Data_Set.csv")

#converting 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')
#df['date'] = pd.to_datetime(df['date'])


#for inspection
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

#dropping null values
df = df.dropna(subset=['open', 'high', 'low'])
print("dataset shape after dropping null values:", df.shape)

#checking for null or missing values
print(df.isnull().sum())

#checking for duplicates
print(df.duplicated().sum())

#reseting index after cleaning
df.reset_index(drop=True, inplace=True)

#to check for failed datatime conversion
#invalid_dates = df['date'].isna().sum()

#import os
#print(os.getcwd())

df.to_csv("cleaned_stock_prices_data_set.csv", index=False)
