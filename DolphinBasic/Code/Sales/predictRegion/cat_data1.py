"""
This program reads sales data from the `SalesData.csv` file, filters it by the specified product category,
and calculates the total sales amount for that category. The program then outputs the total sales amount
of each category in a clear, understandable format.
"""

# Import the necessary libraries
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set the path to the `SalesData.csv` file
CSV_FILE_PATH = "SalesData.csv"

# Read the sales data from the CSV file
with open(CSV_FILE_PATH, mode="r", encoding="ISO-8859-1") as file:
    reader = csv.reader(file)
    header = next(reader)
    sales_data = list(reader)

# Convert the sales data to a Pandas DataFrame, this will make it easier to work with
df = pd.DataFrame(sales_data, columns=header)

# Define the product category to filter the data by
product_category = "Furniture"

# Filter the DataFrame to keep only the rows where the product category is the specified category
filtered_df = df[df["Category"] == product_category]

# Calculate the total sales amount for the specified category
total_sales_amount = filtered_df["Sales"].sum()

# Print the total sales amount for the specified category
print(
    f"The total sales amount for the '{product_category}' category is: ${total_sales_amount}"
)

# Create a bar chart to visualize the total sales amount by product category
sns.set_theme(style="darkgrid")
plt.figure(figsize=(8, 6))
sns.barplot(x="Product Category", y="Sales", data=df)
plt.title("Total Sales Amount by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Sales Amount")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
