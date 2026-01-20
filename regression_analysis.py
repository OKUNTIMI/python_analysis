import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load cleaned dataset
df = pd.read_csv("cleaned_dataset/cleaned_stock_prices_data_set.csv")

# Select features and target
X = df[['open', 'high', 'low', 'volume']]
y = df['close']


# Split the data set for training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    #set random so there would be a fixed value when ever the code is loaded
    random_state=42
)



# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

#predict 
y_pred = model.predict(X_test)

# Show how each feacture affect the "close" value
coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_ 
})

print(coefficients)


# compare test values from prediction values 
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Print The Comapred results
print("R-squared:", r2)
print("Mean Squared Error:", mse)



