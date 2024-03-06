import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

df = pd.read_csv("SalesData.csv", parse_dates=["Order Date", "Ship Date"])

df["Year"] = df["Order Date"].dt.year
df = df[df["Year"] <= 2023]

# Change: Added feature engineering to potentially improve model performance
df["Month"] = df["Order Date"].dt.month  # Added month as a feature

encoder = LabelEncoder()
df["Region_encoded"] = encoder.fit_transform(df["Region"])

aggregated_data = (
    df.groupby(["Year", "Region_encoded", "Month"])["Sales"].sum().reset_index()
)  # Added Month to aggregation

X = aggregated_data[["Year", "Region_encoded", "Month"]]  # Added Month to features
y = aggregated_data["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("Model score:", model.score(X_test, y_test))

predict_data = pd.DataFrame(
    {
        "Year": [2024] * len(encoder.classes_) * 12,  # Repeat for each month of 2024
        "Region_encoded": list(range(len(encoder.classes_)))
        * 12,  # Repeat regions for each month
        "Month": list(range(1, 13))
        * len(encoder.classes_),  # Cycle through months for each region
    }
)

predicted_sales = model.predict(predict_data)

# Sum predictions by region for the entire year of 2024
predicted_sales_sum = {}
for i, region in enumerate(predict_data["Region_encoded"]):
    region_name = encoder.inverse_transform([region])[0]
    if region_name in predicted_sales_sum:
        predicted_sales_sum[region_name] += predicted_sales[i]
    else:
        predicted_sales_sum[region_name] = predicted_sales[i]

regions = list(predicted_sales_sum.keys())
total_predicted_sales = list(predicted_sales_sum.values())

plt.bar(regions, total_predicted_sales)
plt.title("Predicted Sales by Region for 2024")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

highest_sales_region = max(predicted_sales_sum, key=predicted_sales_sum.get)
print(f"Region predicted to have the highest sales in 2024: {highest_sales_region}")
