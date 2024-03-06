import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors

# Load the sales data from the CSV file
df = pd.read_csv("/media/tom/Linux/Python/DolphinBasic/Data/SalesData.csv")

# Create a pivot table to group sales by customer and product
customer_pivot_table = df.pivot_table(
    index="Customer Name", columns="Product Name", values="Sales", aggfunc="sum"
).fillna(0)

# Create a second pivot table for state-based aggregation
state_pivot_table = df.pivot_table(
    index="State", columns="Product Name", values="Sales", aggfunc="sum"
).fillna(0)

# Split the data into training and testing sets for customer data
# (This step isn't directly applicable for NearestNeighbors but kept for consistency)
train_data, _ = train_test_split(customer_pivot_table, test_size=0.2, random_state=42)

# Create a Nearest Neighbors model for customer recommendations
customer_model = NearestNeighbors(metric="cosine", algorithm="brute")
customer_model.fit(train_data)

# No need to split state data; we'll use it as is for state recommendations
# Fit a Nearest Neighbors model for state-based recommendations
state_model = NearestNeighbors(metric="cosine", algorithm="brute")
state_model.fit(state_pivot_table)


def recommend_products(customer_or_state):
    recommendations = []
    if customer_or_state in customer_pivot_table.index:
        # Customer-based recommendation logic (same as before)
        customer_purchases = customer_pivot_table.loc[customer_or_state].values.reshape(
            1, -1
        )
        distances, indices = customer_model.kneighbors(
            customer_purchases, n_neighbors=5
        )

        for i in indices[0]:
            rec_products = train_data.iloc[i]
            recommendations.extend(rec_products[rec_products > 0].index.tolist())

        already_bought = customer_pivot_table.loc[customer_or_state]
        recommendations = [
            product for product in recommendations if not already_bought[product] > 0
        ]

    elif customer_or_state in state_pivot_table.index:
        # State-based recommendation logic
        state_purchases = state_pivot_table.loc[customer_or_state].values.reshape(1, -1)
        distances, indices = state_model.kneighbors(state_purchases, n_neighbors=5)

        for i in indices[0]:
            rec_products = state_pivot_table.iloc[i]
            recommendations.extend(rec_products[rec_products > 0].index.tolist())

        # Assuming we want popular items in the state as recommendations
        recommendations = list(set(recommendations))

    else:
        return "Invalid input. Please enter a valid customer name or state."

    return recommendations


# User interaction
customer_or_state = input("Enter a customer name or state: ")

# Recommend products for the customer or state
recommendations = recommend_products(customer_or_state)

# Print the recommended products
if isinstance(recommendations, list):
    print("Recommended products:", recommendations)
else:
    print(recommendations)
