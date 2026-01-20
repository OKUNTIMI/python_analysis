import pandas as pd

#load datasets
df = pd.read_csv("iris.csv")
df = df.drop_duplicates()


#for inspection
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
#check for null or missing values
print(df.isnull().sum())

#check for duplicates
print(df.duplicated().sum())


#printing the duplicate rows for inspection
#print(df[df.duplicated()])
#print(df[df.duplicated(keep=False)])

#what are the result of all the clening steps?
print("dataset sharp after removing duplicates:", df.shape)

df.to_csv("cleaned_iris.csv", index=False)

#import os 
#print(os.getcwd())