def create_placement_plan(goods):
    """
    Creates a placement plan for goods in a warehouse based on how often they are retrieved adn their size

    Input:
    - goods: A list of tuples, where each tuple contains information about a good
             (name, ID, size, retrieval_frequency).

    Output:
    - A dictionary with the good's name as the key and its location as the value.
    """
    # This line creates the sorted list of items in a way that prioritizes
    # frequency and size
    sorted_goods = sorted(goods, key=lambda x: (-x[3], x[2]))

    # placement_plan is an empty space where the plan will go
    placement_plan = {}
    # This block creates a way to track the items in each section so that no section
    # contains too much "height"
    section_height = {
        f"{aisle}{section}": 0 for aisle in "AB" for section in range(1, 11)
    }

    # This is the way the program checks for the closest unocupied section
    # To the entrance
    def find_next_section(current_aisle, current_section):
        other_aisle = "B" if current_aisle == "A" else "A"
        for section in range(1, 11):
            for aisle in [current_aisle, other_aisle]:
                if section_height[f"{aisle}{section}"] + size <= 4:
                    return aisle, section
        return None, None

    # This code creates a way look at every good in the inputted list
    # and place them in the placement plan
    for good in sorted_goods:
        name, _, size, _ = good
        current_aisle, current_section = find_next_section("A", 1)

        placement_key = f"{current_aisle}{current_section}"
        placement_plan[name] = placement_key
        section_height[placement_key] += size

    return placement_plan


# Example usage
goods = [
    ("HairDryer", 1, 3, 1),
    ("ToothBrush", 2, 1, 2),
    ("HeadSet", 3, 1, 3),
    ("Ipad", 4, 1, 4),
]
placement_plan = create_placement_plan(goods)
print(placement_plan)

# Output: {'Ipad': 'A1', 'HeadSet': 'A1', 'ToothBrush': 'A1', 'HairDryer': 'B1'}
