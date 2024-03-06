import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read sales data from the CSV file
orders_df = pd.read_csv("SalesData.csv", encoding="ISO-8859-1")

# Filter the DataFrame to keep only rows where the product category is the specified one
category_to_analyze = "Furniture"  # Change this to the category you want to analyze
filtered_df = orders_df[orders_df["Category"] == category_to_analyze]

# Group the filtered DataFrame by product category and calculate the total sales amount
category_sales = (
    filtered_df.groupby("Category")
    .agg({"Sales": "sum"})
    .reset_index()
    .rename(columns={"Category": "Product Category", "Sales": "Total Sales"})
)

# Create a bar chart to visualize the total sales amount for each product category
sns.set_theme(style="darkgrid")
plt.figure(figsize=(8, 6))
sns.barplot(x="Product Category", y="Total Sales", data=category_sales)
plt.title(f"Total Sales by Product Category ({category_to_analyze})")
plt.xlabel("Product Category")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
