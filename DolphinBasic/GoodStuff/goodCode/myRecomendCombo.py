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
