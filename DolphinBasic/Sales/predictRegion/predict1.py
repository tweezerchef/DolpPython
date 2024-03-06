import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your DataFrame after loading SalesData.csv
df = pd.read_csv("SalesData.csv", parse_dates=["Order Date"])

# Filter data to include sales up to the year 2023
df = df[df["Order Date"].dt.year <= 2023]

# Extract the year from Order Date for grouping
df["Year"] = df["Order Date"].dt.year

# Aggregate sales by Year and Region
sales_by_year_region = df.groupby(["Year", "Region"])["Sales"].sum().reset_index()

# Pivot the data for easier plotting
pivot_df = sales_by_year_region.pivot(index="Year", columns="Region", values="Sales")

# Plotting
pivot_df.plot(kind="line", marker="o")
plt.title("Annual Sales by Region")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.legend(title="Region")
plt.grid(True)
plt.show()
