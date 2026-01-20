import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load cleaned dataset
df = pd.read_csv("cleaned_dataset/cleaned_stock_prices_data_set.csv")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Filter only PCLN stock
pcln_df = df[df['symbol'] == 'PCLN']

# Sort by date (critical for time series)
pcln_df = pcln_df.sort_values('date')

# Drop missing values (required for decomposition)
pcln_df = pcln_df.dropna(subset=['date', 'close'])

# Plot raw closing price

plt.figure(figsize=(12, 6))
plt.plot(pcln_df['date'], pcln_df['close'], label='Closing Price')

plt.title("PCLN Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.legend()

plt.tight_layout()
plt.show()


# Time series decomposition
pcln_ts = pcln_df.set_index('date')['close']

decomposition = seasonal_decompose(
    pcln_ts,
    model='additive',
    period=30
)

fig = decomposition.plot()
fig.set_size_inches(12, 8)

plt.tight_layout()
plt.show()
