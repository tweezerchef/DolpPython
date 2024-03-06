import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("SalesData.csv", parse_dates=["Order Date", "Ship Date"])

# Data Preparation and Feature Engineering
df["Year"] = df["Order Date"].dt.year

# Filter out future data from the dataset so it is not used to train the model
df = df[df["Year"] <= 2023]

# Encode the categorical 'Region' variable
encoder = LabelEncoder()
df["Region_encoded"] = encoder.fit_transform(df["Region"])

# Aggregate sales by 'Year' and 'Region_encoded'
aggregated_data = df.groupby(["Year", "Region_encoded"])["Sales"].sum().reset_index()

# Prepare the data for the model
X = aggregated_data.drop("Sales", axis=1)
y = aggregated_data["Sales"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize the RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
model_score = model.score(X_test, y_test)

# Print the model score
print("Model score:", model_score)

# Prepare data to predict sales for 2024
predict_data = pd.DataFrame(
    {
        # 'Year' is set to 2024 for all rows
        "Year": [2024] * len(encoder.classes_),
        # 'Region_encoded' is set to each encoded region
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

# Identifying the region with the highest predicted sales
highest_sales_region = regions[predicted_sales.argmax()]
print(f"Region predicted to have the highest sales in 2024: {highest_sales_region}")
