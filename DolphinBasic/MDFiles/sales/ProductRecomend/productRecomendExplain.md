### Introduction

I am a salesperson working for a large company that sells a wide variety of products. Recently, my company sent me a CSV file called `SalesData.csv`. My boss said I should use this data to improve my performance in 2024.

I opened the file up using Google Sheets and saw the columns `Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Discount`, `Profit`.

In each row is a record of every individual sale I closed, with the relevant information for that sale in the appropriate columns. The data begins in 2020 and goes all the way up to the present day in 2024. It looks like a lot of data, and I have no idea how to analyze it. I am not a technically inclined person, I don't know any programming languages, and I have never taken a math class beyond high school algebra.

I asked my friend in the IT department for help, and they recommended that I use the Python programming language to take the data and use it for analysis or other productivity-enhancing tools.

### Issue

 I have a very hard time recommending products to customers. Because I don't make a lot of sales to repeat customers, this makes it even more difficult to predict what to recommend, however I was thinking that maybe the states that the customers order from could be a good indicator of what they might like if combined with each clients purchase history. I asked my friend in the IT department for help, and they came up  with this code to help me out.  They said the code when run would ask me for either an existing client or state and would produce recommendations based on the parameters I had suggested.  Here is that code they sent me:

```Python
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load the sales data from the CSV file (Please change if not in current directory)
df = pd.read_csv("SalesData.csv")

# Create two "pivot tables"
customer_pivot_table = df.pivot_table(
    index="Customer Name", columns="Product Name", values="Sales", aggfunc="sum"
).fillna(0)


state_pivot_table = df.pivot_table(
    index="State", columns="Product Name", values="Sales", aggfunc="sum"
).fillna(0)

# Use nearest neighbor model
customer_model = NearestNeighbors(metric="cosine", algorithm="brute")
customer_model.fit(customer_pivot_table)

# Fit a Nearest Neighbors model for state-based recommendations
state_model = NearestNeighbors(metric="cosine", algorithm="brute")
state_model.fit(state_pivot_table)


#  function to run recommendation agent
def recommend_products(customer_name, state=None):
    recommendations = set()
    state_recommendations = set()

    if customer_name in customer_pivot_table.index:
        customer_purchases = customer_pivot_table.loc[customer_name].values.reshape(
            1, -1
        )
        _, indices = customer_model.kneighbors(customer_purchases, n_neighbors=5)

        for i in indices[0]:
            rec_products = customer_pivot_table.iloc[i]
            recommendations.update(rec_products[rec_products > 0].index)

        already_bought = set(
            customer_pivot_table.loc[customer_name][
                customer_pivot_table.loc[customer_name] > 0
            ].index
        )
        recommendations -= already_bought

    if not state and customer_name in df["Customer Name"].values:
        state = df[df["Customer Name"] == customer_name]["State"].values[0]

    if state and state in state_pivot_table.index:
        state_purchases = state_pivot_table.loc[state].values.reshape(1, -1)
        _, indices = state_model.kneighbors(state_purchases, n_neighbors=5)

        for i in indices[0]:
            rec_products = state_pivot_table.iloc[i]
            state_recommendations.update(rec_products[rec_products > 0].index)

        recommendations = recommendations.union(state_recommendations)

    # Return the top 10 recommendations
    return list(recommendations)[:10]


#  Creates user inputs
customer_name = input("Enter a customer name (leave blank if new customer): ")
state = input("Enter state (if known or new customer): ") if not customer_name else None

# run the recommendation agent for the users inputs
recommendations = recommend_products(customer_name, state)

# Print the recommended products
print(
    "Recommended products:",
    recommendations if recommendations else "No recommendations available.",
)
```

### Issue

The program itself seems to work perfectly.  It also includes some comments to help me understand how it works.  However, I really need to understand certain aspects in a more in depth manner.  I am not technically inclined at all, and never took a statistics class, but I want to learn how to create similar programs on my own, and understand machine learning, statistics, Python and its various libraries much better.

### Task at Hand

I need you to go above and beyond the comments in the code and explain to me in plain English. Please explain specific details in particular as listed below.

1. Explain all data science, statistics, and machine learning concepts and terms used in the code.
2. Explain the purpose of each library used in the code.
3. Explain how each invocation of a library function works, what it does and what it can do in other contexts.
4. In a sense I would like you to use this code as a starting point to teach me about data science, statistics, Python and machine learning.  I would like to understand the code and the concepts behind it as if I were taking a class on the subject.

### Summary

1. Please use a bullet point list to explain all the details listed above.
2. You should add the line or block of code you are explaining or using for the explanation in the bullet point list. Please include it as part of the list but use markdown to format it as code.
3. Please use plain English and avoid technical jargon as much as possible.  If you must use technical jargon, please explain it in a way that a high school freshman could understand.
4. After you have created this explanation, please return it to me. Please do not include the entire original program that I want explained, only the explanation in bullet point form.
