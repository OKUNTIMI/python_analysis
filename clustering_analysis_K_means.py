import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

from sklearn.cluster import KMeans
import seaborn as sns



# Load cleaned dataset
df = pd.read_csv("cleaned_dataset/cleaned_stock_prices_data_set.csv")

# Select numerical features for clustering
features = df[['open', 'high', 'low', 'close', 'volume']]

# Drop missing values (important for K-Means)
features = features.dropna()

# Initialize the scaler
scaler = StandardScaler()

# Standardize the features
scaled_features = scaler.fit_transform(features)
 
inertia_values = []

# Test K values from 1 to 10
for k in range(1, 11):
    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    kmeans.fit(scaled_features)
    inertia_values.append(kmeans.inertia_)

#plot a line chart to show the elbow method for optimal K
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia_values, marker='o')

plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")

plt.tight_layout()
plt.show()



# Choose optimal number of clusters
k = 10
kmeans = KMeans(
    n_clusters=k,
    random_state=42,
    n_init=10
)

# Fit model and assign clusters
clusters = kmeans.fit_predict(scaled_features)

# Add cluster labels to original dataframe
df['cluster'] = clusters



plt.figure(figsize=(10, 6))

sns.scatterplot(
    x=df['open'],
    y=df['close'],
    hue=df['cluster'],
    palette='viridis',
    alpha=0.7
)

plt.title("K-Means Clustering of Stocks (Open vs Close Price)")
plt.xlabel("Opening Price")
plt.ylabel("Closing Price")
plt.legend(title="Cluster")

plt.tight_layout()
plt.show()
