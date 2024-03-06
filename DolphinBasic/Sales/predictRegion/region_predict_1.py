import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the sales data from the CSV file
df = pd.read_csv("SalesData.csv", parse_dates=["Order Date"])

# Filter the data for sales in 2020-2023
df = df[df["Order Date"].dt.year <= 2023]

# Group the data by region and year to calculate the total sales for each region
df_region_sales = (
    df.groupby(["Region", pd.Grouper(key="Order Date", freq="Y")])["Sales"]
    .sum()
    .reset_index(name="Total Sales")
)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    df_region_sales["Order Date"].dt.year.values.reshape(-1, 1),
    df_region_sales["Total Sales"].values.reshape(-1, 1),
)

# Create a linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Predict the sales for 2024
year = 2024
predicted_sales = model.predict(np.array(year).reshape(-1, 1))

# Get the region with the highest predicted sales
region_with_highest_sales = df_region_sales["Region"][np.argmax(predicted_sales)]

# Print the predicted region
print("Region with the highest predicted sales in 2024:", region_with_highest_sales)

# Plot the predicted sales for each region
plt.bar(df_region_sales["Region"], predicted_sales)
plt.title("Predicted Sales by Region in 2024")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()
