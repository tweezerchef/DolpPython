import numpy as np


# Define a class to represent the warehouse
class Warehouse:
    def __init__(self, num_aisles, num_sections):
        # Initialize the number of aisles and sections
        self.num_aisles = num_aisles
        self.num_sections = num_sections

        # Create a 2D array to represent the warehouse grid
        self.grid = np.zeros((num_aisles, num_sections), dtype=object)


# Function to calculate the distance from a given section to the entrance
def calculate_distance(aisle, section):
    # The entrance is located at the center bottom edge of the grid
    entrance_location = (0, num_sections // 2)

    # Calculate the distance using the Manhattan distance formula
    distance = abs(aisle - entrance_location[0]) + abs(section - entrance_location[1])

    return distance


# Function to place the goods in the warehouse
def optimize_placement(goods):
    # Create a warehouse object
    warehouse = Warehouse(2, 10)

    # Sort the goods in descending order of retrieval frequency
    sorted_goods = sorted(goods, key=lambda x: x[3], reverse=True)

    # Iterate over the sorted goods and place them in the warehouse
    for good in sorted_goods:
        name, _, size, _ = good

        # Find the available section with the lowest distance and available capacity
        best_aisle = None
        best_section = None
        best_distance = float("inf")

        for aisle in range(warehouse.num_aisles):
            for section in range(warehouse.num_sections):
                # Check if the section is empty and has enough capacity
                if (
                    warehouse.grid[aisle][section] is None
                    and sum(warehouse.grid[aisle]) + size <= 4
                ):
                    distance = calculate_distance(aisle, section)
                    if distance < best_distance:
                        best_aisle = aisle
                        best_section = section
                        best_distance = distance

        # Place the good in the best available section
        warehouse.grid[best_aisle][best_section] = name

    # Create a placement plan dictionary
    placement_plan = {}
    for aisle in range(warehouse.num_aisles):
        for section in range(warehouse.num_sections):
            if warehouse.grid[aisle][section] is not None:
                placement_plan[warehouse.grid[aisle][section]] = (
                    f"{chr(ord('A') + aisle)}{section + 1}"
                )

    return placement_plan


goods = [
    ("HairDryer", 1, 3, 1),
    ("ToothBrush", 2, 1, 2),
    ("HeadSet", 3, 1, 3),
    ("Ipad", 4, 1, 4),
]
placement_plan = optimize_placement(goods)
print(placement_plan)
