import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the sales data from the CSV file
df = pd.read_csv("SalesData.csv", parse_dates=["Order Date"])

# Filter the data to include sales from 2020 to 2023
df = df[df["Order Date"].dt.year.between(2020, 2023)]

# Group the data by region and calculate the total sales
sales_by_region = df.groupby("Region")["Sales"].sum().reset_index()

# Create a linear regression model
model = LinearRegression()

# Train the model using the historical sales data
X = sales_by_region["Region"].values.reshape(-1, 1)
y = sales_by_region["Sales"].values
model.fit(X, y)

# Predict the sales for each region in 2024
regions = ["South", "East", "Central", "West"]
predicted_sales = model.predict(np.array(regions).reshape(-1, 1))

# Visualize the predicted sales
plt.bar(regions, predicted_sales)
plt.title("Predicted Sales by Region in 2024")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# Print the predicted region with the highest sales
predicted_region = regions[np.argmax(predicted_sales)]
print(f"The region predicted to have the highest sales in 2024 is: {predicted_region}")
