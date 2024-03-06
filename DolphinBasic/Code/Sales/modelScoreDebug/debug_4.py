import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_percentage_error

# Load the dataset
df = pd.read_csv("SalesData.csv", parse_dates=["Order Date", "Ship Date"])

# Filter out future sales
df = df[df["Year"] <= 2023]

# Encode the categorical 'Region' variable
encoder = LabelEncoder()
df["Region_encoded"] = encoder.fit_transform(df["Region"])

# Group the data by year and region to calculate total sales
aggregated_data = df.groupby(["Year", "Region_encoded"])["Sales"].sum().reset_index()

# Split the data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(
    aggregated_data.drop("Sales", axis=1),
    aggregated_data["Sales"],
    test_size=0.2,
    random_state=42,
)

# Initialize the RandomForestRegressor model with 100 trees
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
predicted_sales_test = model.predict(X_test)

# Evaluate the model using MAPE - 1 - MAPE indicates the accuracy of the model
mape = mean_absolute_percentage_error(y_test, predicted_sales_test)
print("Model score:", 1 - mape)

# Prepare data for 2024 prediction
predict_data = pd.DataFrame(
    {
        # The year for which we want predictions
        "Year": [2024] * len(encoder.classes_),
        # Encoded region values
        "Region_encoded": range(len(encoder.classes_)),
    }
)

# Make predictions for 2024 sales
predicted_sales_2024 = model.predict(predict_data)

# Visualize the predicted sales by region for 2024
regions = encoder.inverse_transform(predict_data["Region_encoded"])
plt.bar(regions, predicted_sales_2024)
plt.title("Predicted Sales by Region for 2024")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Identify the region with the highest predicted sales
highest_sales_region = regions[predicted_sales_2024.argmax()]
print(f"Region predicted to have the highest sales in 2024: {highest_sales_region}")
