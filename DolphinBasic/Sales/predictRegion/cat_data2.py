# Import the required libraries for data manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the sales data from the CSV file
sales_df = pd.read_csv("SalesData.csv", encoding="ISO-8859-1")

# Select the 'Product Category' and 'Sales' columns from the DataFrame
category_sales_df = sales_df[["Category", "Sales"]]

# Group the data by 'Product Category' and sum the 'Sales'
category_sales_sum_df = category_sales_df.groupby("Category").sum()

# Reset the index to convert 'Product Category' back to a column
category_sales_sum_df = category_sales_sum_df.reset_index()

# Create a bar chart to visualize the total sales by product category
sns.set_theme(style="darkgrid")
plt.figure(figsize=(8, 6))
sns.barplot(x="Category", y="Sales", data=category_sales_sum_df)
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Display the bar chart
plt.show()

# Print the total sales amount for each product category to the console
print("\nTotal Sales by Product Category:")
for index, row in category_sales_sum_df.iterrows():
    print(f"  {row['Product Category']}: ${row['Sales']:.2f}")
