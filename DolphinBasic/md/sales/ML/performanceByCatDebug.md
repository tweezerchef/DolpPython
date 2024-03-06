### Introduction

I am a salesperson for a large company that sells a huge variety of products. Recently my company sent me this huge CSV file `SalesData.cvs`.

I opened it up using Google Sheets and saw the columns `Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Discount`, `Profit`. In each row was a record of every individual sale I closed, with the relevant information in the appropriate columns. It looks like a lot of data, and I have no idea how to analyze it, but it seems to track all of my sales.

I asked my friend in the IT department for help, and he recommended that I use the Python programming language to take all the data and use it for analysis.

### Task

The first thing I wanted to do was to see how all the different type of products, listed in the `Category` column, were performing by type. So that I could alter my strategies based on the data. I asked my friend to help me, and they gave me this Python program which they said reads the sales data from the `SalesData.csv` file, filters it by the product type in the category column, and outputs a bar chart of the total sales amount for each type, with the exact dollar amount for each category type in numerical form as well. Here is that code:

```Python
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

```

### Issue

The code works well overall.  When I run it in Visual Studio Code, it opens a window with the correct-looking data in bar chart form. However, it never prints the total sales amount for each product category to the console. Also, when I close the bar chart window, this error appears:

```python console

$ /usr/bin/python3 /media/tom/Linux/Python/DolphinBasic/Sales/cat_data2.py

Total Sales by Product Category:
Traceback (most recent call last):
  File "/home/tom/.local/lib/python3.10/site-packages/pandas/core/indexes/base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Product Category'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/media/tom/Linux/Python/DolphinBasic/Sales/cat_data2.py", line 34, in <module>
    print(f"  {row['Product Category']}: ${row['Sales']:.2f}")
  File "/home/tom/.local/lib/python3.10/site-packages/pandas/core/series.py", line 1112, in __getitem__
    return self._get_value(key)
  File "/home/tom/.local/lib/python3.10/site-packages/pandas/core/series.py", line 1228, in _get_value
    loc = self.index.get_loc(label)
  File "/home/tom/.local/lib/python3.10/site-packages/pandas/core/indexes/base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 'Product Category'
```

### Solution

* Please debug and fix the code so this error does not appear.
* Please add the total sales amount for each product category, in dollar amount,  to the bar chart so I can see the information in one place.
* Please create a summary of what the error was and how you fixed it.  I want to learn from your code, so please explain the code as if you were teaching a high school student how to use Python.
* Respond with the summary in plain text followed by the debugged and fixed Python code.
