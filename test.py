import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load cleaned dataset
df = pd.read_csv("cleaned_dataset/cleaned_stock_prices_data_set.csv")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter only PCLN stock
pcln_df = df[df['symbol'] == 'PCLN']

# Sort by date (critical for time series)
pcln_df = pcln_df.sort_values('date')

print(df.shape)
df = df.groupby([df['date'].dt.year , 'symbol']).mean()
print(df)
