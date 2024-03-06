import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the sales data from the CSV file
df = pd.read_csv("/media/tom/Linux/Python/DolphinBasic/Data/SalesData.csv")

# Group the data by customer ID and state
customer_state_groups = df.groupby(["Customer ID", "State"])

# Create a dictionary to store the product recommendations for each customer and state
recommendations = {}

# Iterate over each customer and state group
for (customer_id, state), group in customer_state_groups:
    # Get the products purchased by the customer in the given state
    customer_products = group["Product ID"].unique()

    # Get the products purchased by other customers in the same state
    state_products = df[df["State"] == state]["Product ID"].unique()

    # Get the products that the customer has not purchased but others in their state have
    recommended_products = list(set(state_products) - set(customer_products))

    # Store the recommended products for the customer and state
    recommendations[(customer_id, state)] = recommended_products


# Create a function to generate product recommendations for a given customer or state
def get_recommendations(customer_name=None, state=None):
    # Check if both customer name and state are provided
    if customer_name and state:
        # Get the recommendations for the specified customer and state
        return recommendations[(customer_name, state)]

    # Check if only customer name is provided
    elif customer_name:
        # Get the recommendations for all states where the customer has made purchases
        customer_states = df[df["Customer Name"] == customer_name]["State"].unique()
        return [
            product
            for s in customer_states
            for product in recommendations[(customer_name, s)]
        ]

    # Check if only state is provided
    elif state:
        # Get the recommendations for all customers in the specified state
        customer_ids = df[df["State"] == state]["Customer ID"].unique()
        return [
            product for c in customer_ids for product in recommendations[(c, state)]
        ]

    # Otherwise, return an error message
    else:
        return "Please provide either a customer name or a state."


# Create a function to evaluate the recommendation engine
def evaluate_model():
    # Split the data into training and testing sets
    train_df, test_df = train_test_split(df, test_size=0.2)

    # Create a K-Nearest Neighbors classifier
    knn = KNeighborsClassifier(n_neighbors=5)

    # Train the model on the training data
    knn.fit(train_df[["Customer ID", "State", "Product ID"]], train_df["Sales"])

    # Predict the sales on the testing data
    predictions = knn.predict(test_df[["Customer ID", "State", "Product ID"]])

    # Calculate the accuracy of the model
    accuracy = accuracy_score(test_df["Sales"], predictions)

    # Return the model score
    return accuracy


# Prompt the user for input
customer_name = input("Enter a customer name or leave blank: ")
state = input("Enter a state or leave blank: ")

# Get the product recommendations
recommendations = get_recommendations(customer_name, state)

# Print the recommended products
print("Recommended products:")
for product in recommendations:
    print(product)

# Evaluate the recommendation engine
model_score = evaluate_model()

# Print the model score
print("Model score:", model_score)
