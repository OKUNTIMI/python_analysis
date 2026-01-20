import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the cleaned_stock_prices_data_set
df = pd.read_csv("cleaned_dataset\cleaned_stock_prices_data_set.csv")

#converting 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')



#(
#for inspection
#print(df.head())
#print(df.info())

#Numerical summary
print(df[['open','high','low','close','volume']].describe())

#Explicit means, median, mode 
#print("Mean:\n", df[['open','high','low','close','volume']].mean())
#print("\nMedian:\n", df[['open','high','low','close','volume']].median())
#print("\nMode:\n", df[['open','high','low','close','volume']].mode())

#Histogram 
#df[['open', 'close']].hist(figsize=(10,4)) 
#plt.show()

#Boxplots 
#plt.figure(figsize=(8,4))
#sns.boxplot(data=df[['open','close']])
#plt.show()

#scatter plot: open vs close
#sns.scatterplot(x='open',y='close',data=df,alpha=0.5)
#plt.show()

#Correlationn matix
#corr = df[['open','high','low','close','volume']].corr()
#print(corr)

#plt.figure(figsize=(8,6))
#sns.heatmap(corr, annot=True, cmap='coolwarm')
#plt.show()



#I had an issues of charts loading once at a time and only loading the next chart after the currently displalyed on has beeen clossed
#So my fix is to make them all displayed at once 
#i will comment the charts created above so i dont have to deal with it when i run my code 


# Create a large figure
fig, axes = plt.subplots(3, 2, figsize=(15, 14))
fig.suptitle("Exploratory Data Analysis (EDA) – Stock Market Data", fontsize=18)


# 1. Histogram: Open Price
sns.histplot(df['open'], kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Distribution of Opening Prices")
axes[0, 0].set_xlabel("Open Price")
axes[0, 0].set_ylabel("Frequency")

# 2. Histogram: Close Price
sns.histplot(df['close'], kde=True, ax=axes[0, 1])
axes[0, 1].set_title("Distribution of Closing Prices")
axes[0, 1].set_xlabel("Close Price")
axes[0, 1].set_ylabel("Frequency")


# 3. Boxplot: Open vs Close
sns.boxplot(data=df[['open', 'close']], ax=axes[1, 0])
axes[1, 0].set_title("Boxplot of Open and Close Prices")
axes[1, 0].set_ylabel("Price")


# 4. Scatter Plot: Open vs Close
sns.scatterplot(
    x='open',
    y='close',
    data=df,
    alpha=0.5,
    ax=axes[1, 1]
)
axes[1, 1].set_title("Relationship Between Open and Close Prices")
axes[1, 1].set_xlabel("Open Price")
axes[1, 1].set_ylabel("Close Price")


# 5. Correlation Heatmap
corr = df[['open', 'high', 'low', 'close', 'volume']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[2, 0])
axes[2, 0].set_title("Correlation Between Numerical Features")


# Empty subplot (clean layout)
axes[2, 1].axis('off')

# Adjust layout so titles don't overlap
plt.tight_layout(rect=[0, 0, 1, 0.9])

# Show all plots at once
plt.show()
