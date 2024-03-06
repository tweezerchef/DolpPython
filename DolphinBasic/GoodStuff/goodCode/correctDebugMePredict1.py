import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the sales data from the CSV file
df = pd.read_csv("SalesData.csv", parse_dates=["Order Date"])

# Ensure the data is for sales in 2020-2023
df = df[df["Order Date"].dt.year <= 2023]

# Encode the region strings as numbers, in order to work in linear regression
df["Region_encoded"] = df["Region"].astype("category").cat.codes

# Group the data by region and year to calculate the total sales for each region
df["Year"] = df["Order Date"].dt.year
df_region_sales = df.groupby(["Region_encoded", "Year"])["Sales"].sum().reset_index()

# Prepare the data for Linear Regression

X = df_region_sales[["Region_encoded", "Year"]]
y = df_region_sales["Sales"]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Prepare data for prediction: all regions for the year 2024
predict_data = pd.DataFrame(
    {"Region_encoded": np.sort(df["Region_encoded"].unique()), "Year": 2024}
)

# Create predicted sales data
predicted_sales = model.predict(predict_data)
print("Model score:", model.score(X_test, y_test))
# Reverse back the encoded "Region" into the human readable strings the encoded numbers represent
predict_data["Region"] = predict_data["Region_encoded"].map(
    dict(enumerate(df["Region"].astype("category").cat.categories))
)

# Plot the predicted sales for each region, as a bar chart in order to create a visualization of the data
plt.figure(figsize=(10, 6))
plt.bar(predict_data["Region"], predicted_sales, color="skyblue")
plt.title("Predicted Sales by Region in 2024")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Identify the region with the highest predicted sales and print the region name when the bar chart window is closed.
index_of_max = np.argmax(predicted_sales)
region_with_highest_sales = predict_data.iloc[index_of_max]["Region"]
print(f"Region with the highest predicted sales in 2024: {region_with_highest_sales}")
