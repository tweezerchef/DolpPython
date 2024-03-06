import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors

# Load the sales data from the CSV file
df = pd.read_csv("/media/tom/Linux/Python/DolphinBasic/Data/SalesData.csv")

# Create a pivot table to group sales by customer and product
pivot_table = df.pivot_table(
    index="Customer Name", columns="Product Name", values="Sales", aggfunc="sum"
).fillna(0)

# Split the data into training and testing sets (this step isn't directly applicable for NearestNeighbors but let's keep for consistency)
train_data, test_data = train_test_split(pivot_table, test_size=0.2, random_state=42)

# Create a Nearest Neighbors model
model = NearestNeighbors(metric="cosine", algorithm="brute")
model.fit(train_data)


def recommend_products(customer_or_state):
    recommendations = []
    if customer_or_state in pivot_table.index:
        customer_purchases = pivot_table.loc[customer_or_state].values.reshape(1, -1)
        distances, indices = model.kneighbors(customer_purchases, n_neighbors=5)

        for i in indices[0]:
            rec_products = train_data.iloc[i]
            recommendations.extend(rec_products[rec_products > 0].index.tolist())

        # Filter out the products the customer already bought
        already_bought = pivot_table.loc[customer_or_state]
        recommendations = [
            product for product in recommendations if not already_bought[product] > 0
        ]

    elif customer_or_state in df["State"].unique():
        # This part of the logic needs more detail on how you intend to recommend based on state since your pivot table is by Customer Name x Product Name
        print("State-based recommendation not directly supported with current setup.")
        return []

    else:
        return "Invalid input. Please enter a valid customer name or state."

    return list(set(recommendations))  # Return unique recommendations


# User interaction
customer_or_state = input("Enter a customer name or state: ")

# Recommend products for the customer or state
recommendations = recommend_products(customer_or_state)

# Print the recommended products
if isinstance(recommendations, list):
    print("Recommended products:", recommendations)
else:
    print(recommendations)
