import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# Load the dataset
df = pd.read_csv("SalesData.csv", parse_dates=["Order Date", "Ship Date"])

# Data Preparation and Feature Engineering
df["Year"] = df["Order Date"].dt.year

# Keep only data up to 2023 as training data
df = df[df["Year"] <= 2023]

# Encode the categorical 'Region' variable
encoder = LabelEncoder()
df["Region_encoded"] = encoder.fit_transform(df["Region"])

# Aggregate sales by Year and Region_encoded
aggregated_data = df.groupby(["Year", "Region_encoded"])["Sales"].sum().reset_index()

# Prepare the data
X = aggregated_data[["Year", "Region_encoded"]]
y = aggregated_data["Sales"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize the RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the model score (using mean squared error)
model_score = mean_squared_error(
    y_test, y_pred, squared=False
)  # Calculate RMSE instead of MAE

# Print the model score
print("Model score (RMSE):", model_score**0.5)

# Prepare data for 2024 prediction
# Note: This step assumes you have encoded regions as before and '2024' is the year you want predictions for.
predict_data = pd.DataFrame(
    {
        "Year": [2024] * len(encoder.classes_),
        "Region_encoded": range(len(encoder.classes_)),
    }
)

# Predict sales for 2024
predicted_sales = model.predict(predict_data)

# Visualization
regions = encoder.inverse_transform(predict_data["Region_encoded"])
plt.bar(regions, predicted_sales)
plt.title("Predicted Sales by Region for 2024")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Identify the region with the highest predicted sales
highest_sales_region = regions[predicted_sales.argmax()]

# Print the region with the highest predicted sales
print(f"Region predicted to have the highest sales in 2024: {highest_sales_region}")
