# Import the necessary libraries
import pandas as pd  # For data manipulation and sorting

# Define the warehouse dimensions
AISLES = 2
SECTIONS_PER_AISLE = 10

# Define the maximum height capacity per section
MAX_HEIGHT_PER_SECTION = 4


# Create a function to generate the placement plan
def optimize_placement(goods):
    """
    This function takes a list of goods and returns a placement plan that minimizes retrieval time.

    Args:
        goods: A list of tuples containing the good's name, ID, size, and retrieval frequency.

    Returns:
        A dictionary with the good's name as the key and the location as the value.
    """

    # Convert the list of goods into a Pandas DataFrame for easier data manipulation
    df = pd.DataFrame(goods, columns=["Name", "ID", "Size", "Frequency"])

    # Sort the DataFrame in descending order of retrieval frequency
    df = df.sort_values("Frequency", ascending=False)

    # Create a dictionary to store the placement plan
    placement_plan = {}

    # Iterate through the sorted DataFrame and assign locations to the goods
    for _, row in df.iterrows():
        # Get the good's name, size, and frequency
        name = row["Name"]
        size = row["Size"]
        frequency = row["Frequency"]

        # Find the best location for the good based on its size and frequency
        for aisle in range(AISLES):
            for section in range(SECTIONS_PER_AISLE):
                # Calculate the section's location as a string
                location = f"{'A' + str(aisle)}{str(section) + 1}"

                # Check if the section has enough space for the good
                if (
                    location not in placement_plan.values()
                    and MAX_HEIGHT_PER_SECTION
                    - sum(
                        placement_plan.get(good, 0)
                        for good in placement_plan
                        if placement_plan[good].startswith(f"{'A' + str(aisle)}")
                    )
                    >= size
                ):
                    # Assign the good to the location
                    placement_plan[name] = location
                    break

    # Return the placement plan
    return placement_plan


# Example usage:
goods = [
    ("HairDryer", 1, 3, 1),
    ("ToothBrush", 2, 1, 2),
    ("HeadSet", 3, 1, 3),
    ("Ipad", 4, 1, 4),
]

# Generate the placement plan
placement_plan = optimize_placement(goods)

# Print the placement plan
print(placement_plan)
