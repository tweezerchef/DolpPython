def create_placement_plan(goods):
    # This line creates the sorted list of items in a way that prioritizes
    # frequency and size
    sorted_goods = sorted(goods, key=lambda x: (-x[3], x[2]))

    # placement_plan is an empty space where the plan will go
    placement_plan = {}

    # This block creates a way to track the items in each section so that no section
    # contains too much "height"
    current_aisle = "A"
    current_section = 1
    section_height = {f"A{i}": 0 for i in range(1, 11)}
    section_height.update({f"B{i}": 0 for i in range(1, 11)})

    # This code creates a way look at every good in the inputted list
    for good in sorted_goods:
        name, _, size, _ = good

        # This checks if a section has enough space to hold the item
        # If not, move to the next section or aisle.
        if section_height[current_aisle + str(current_section)] + size > 4:
            current_section += 1
            if current_section > 10:
                current_section = 1
                current_aisle = "B" if current_aisle == "A" else "A"

        # These lines add the item to the placement plan and record the results
        # of adding the additional item to a section.
        placement_plan[name] = current_aisle + str(current_section)
        section_height[current_aisle + str(current_section)] += size

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
# {'Ipad': 'A1', 'HeadSet': 'A1', 'ToothBrush': 'A1', 'HairDryer': 'A2'}
