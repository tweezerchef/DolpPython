import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import NearestNeighbors

# Load the sales data from the CSV file
df = pd.read_csv("/media/tom/Linux/Python/DolphinBasic/Data/SalesData.csv")

# Create a pivot table to group sales by customer and product
pivot_table = df.pivot_table(
    index="Customer Name", columns="Product Name", values="Sales"
)

# Fill in missing values with 0
pivot_table = pivot_table.fillna(0)

# Split the data into training and testing sets
train_data, test_data = train_test_split(pivot_table, test_size=0.2)

# Create a Nearest Neighbors model
model = NearestNeighbors(metric="cosine", algorithm="brute")
model.fit(train_data)


# Function to recommend products for a given customer or state
def recommend_products(customer_or_state):
    if customer_or_state in pivot_table.index:
        # If the input is a customer name, get their purchase history
        customer_purchases = pivot_table.loc[customer_or_state]

        # Find the nearest neighbors to the customer
        distances, indices = model.kneighbors(
            customer_purchases.values.reshape(1, -1), n_neighbors=5
        )

        # Get the products purchased by the nearest neighbors
        neighbor_purchases = train_data.iloc[indices[0]]

        # Recommend products that the customer has not purchased before
        recommendations = neighbor_purchases[
            ~customer_purchases.index.isin(neighbor_purchases.index)
        ]
        recommendations = recommendations.sort_values(ascending=False)

    elif customer_or_state in df["State"].unique():
        # If the input is a state, get the purchase history of customers in that state
        state_purchases = pivot_table.loc[df["State"] == customer_or_state]

        # Find the average purchase history for the state
        avg_state_purchases = state_purchases.mean()

        # Find the nearest neighbors to the average state purchase history
        distances, indices = model.kneighbors(
            avg_state_purchases.values.reshape(1, -1), n_neighbors=5
        )

        # Get the products purchased by the nearest neighbors
        neighbor_purchases = train_data.iloc[indices[0]]

        # Recommend products that are popular in the state but have not been purchased by the customer
        recommendations = neighbor_purchases[
            ~pivot_table.loc[customer_or_state].index.isin(neighbor_purchases.index)
        ]
        recommendations = recommendations.sort_values(ascending=False)

    else:
        # If the input is not a valid customer name or state, return an error message
        return "Invalid input. Please enter a valid customer name or state."

    # Return the recommended products
    return recommendations.index.tolist()


# Function to calculate the model score
def get_model_score():
    predictions = model.predict(test_data)
    rmse = mean_squared_error(test_data, predictions, squared=False)
    return rmse


# Get the user input
customer_or_state = input("Enter a customer name or state: ")

# Recommend products for the customer or state
recommendations = recommend_products(customer_or_state)

# Print the recommended products
print("Recommended products:", recommendations)

# Print the model score
model_score = get_model_score()
print("Model score:", model_score)
