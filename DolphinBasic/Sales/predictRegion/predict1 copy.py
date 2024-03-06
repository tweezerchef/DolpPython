import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data
df = pd.read_csv("SalesData.csv", parse_dates=["Order Date", "Ship Date"])

# Prepare the data: Filter records up to 2023 and extract the year from the order date
df = df[df["Order Date"].dt.year <= 2023]
df["Year"] = df["Order Date"].dt.year

# Group the data by year and region, then sum up the sales
sales_trends = df.groupby(["Year", "Region"])["Sales"].sum().unstack()

# Visualize sales trends by region
sales_trends.plot(kind="line", marker="o")
plt.title("Sales Trends by Region (2020-2023)")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.legend(title="Region")
plt.grid(True)
plt.show()

# Estimating which region will have the highest sales in 2024 based on past trends
# Note: This is a simplified estimation and may not reflect complex market dynamics
growth_rates = sales_trends.pct_change().mean()
predicted_growth = sales_trends.iloc[-1] * (1 + growth_rates)
predicted_highest_sales_region = predicted_growth.idxmax()

print(
    f"Based on past sales trends, the region predicted to have the highest sales in 2024 is: {predicted_highest_sales_region}"
)
