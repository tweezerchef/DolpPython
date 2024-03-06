"""
This program reads sales data from a CSV file, filters it by the specified product category,
and calculates the total sales amount for that category. The program then outputs the total sales
amount of each category in a clear, understandable format.
"""

# Import the necessary libraries for data manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the sales data from the CSV file into a Pandas DataFrame, skip the first row as it contains the column headers
df = pd.read_csv("SalesData.csv", encoding="ISO-8859-1")

# Prompt the user to enter the product category they want to analyze
product_category = input("Enter the product category you want to analyze: ")

# Filter the DataFrame by the specified product category
filtered_df = df[df["Category"] == product_category]

# Calculate the total sales amount for the specified product category
total_sales_amount = filtered_df["Sales"].sum()

# Create a bar chart to visualize the total sales amount for the specified product category
sns.set_theme(style="darkgrid")
plt.figure(figsize=(8, 6))
sns.barplot(x="Category", y="Sales", data=filtered_df)
plt.title(f"Total Sales by Category: {product_category}")
plt.xlabel("Category")
plt.ylabel("Sales")

# Rotate the x-axis labels
plt.xticks(rotation=90)

# Display the bar chart
plt.show()

# Print the total sales amount for the specified product category to the console
print(
    f"The total sales amount for the specified product category ({product_category}) is: ${total_sales_amount:.2f}"
)
