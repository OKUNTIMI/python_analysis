import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned stock data
df = pd.read_csv("cleaned_dataset\cleaned_stock_prices_data_set.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

#1. Calculate average closing price per stock
avg_close = df.groupby('symbol')['close'].mean().reset_index()

#sort out the top 10 stocks by average closing price for better visualization
top20 = avg_close.sort_values(by='close', ascending=False).head(20)


plt.figure(figsize=(10, 5))
sns.barplot(x='symbol', y='close', data=top20 )

#labeling the plot
plt.title("Average Closing Price by Stock Symbol")
plt.xlabel("Stock Symbol")
plt.ylabel("Average Closing Price")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Bar_plot_Dv_spds.png")
plt.show()

#2. line chart
# selected the highest stock from the barplot 
chosen_symbol = "PCLN"
sample_stock = df[df['symbol'] == chosen_symbol]

plt.figure(figsize=(10, 5))
plt.plot(
    sample_stock['date'],
    sample_stock['close'],
    label="Closing Price"
)

plt.title(f"Closing Price Trend for {chosen_symbol}")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.legend()

plt.tight_layout()
plt.savefig("line_chart_Dv_spds.png")
plt.show()


#3. Scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x='open',
    y='close',
    data=df,
    alpha=0.5
)

plt.title("Relationship Between Open and Close Prices")
plt.xlabel("Open Price")
plt.ylabel("Close Price")

plt.tight_layout()
plt.savefig("Scatter_plot_Dv_spds.png")
plt.show()
