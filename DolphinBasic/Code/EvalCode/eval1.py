# Define the conversion factors between units
tablespoons_per_teaspoon = 3
cups_per_tablespoon = 1 / 16
quarts_per_cup = 1 / 4
gallons_per_quart = 1 / 4


# Define a function to convert from one unit to another
def convert_units(amount, from_unit, to_unit):
    # Check if the units are valid
    if from_unit not in ["tablespoon", "teaspoon", "cup", "quart", "gallon"]:
        raise ValueError("Invalid from unit.")
    if to_unit not in ["tablespoon", "teaspoon", "cup", "quart", "gallon"]:
        raise ValueError("Invalid to unit.")

    # Convert the amount to tablespoons
    if from_unit == "teaspoon":
        amount /= teaspoons_per_teaspoon
    elif from_unit == "cup":
        amount *= cups_per_tablespoon
    elif from_unit == "quart":
        amount *= quarts_per_cup * cups_per_tablespoon
    elif from_unit == "gallon":
        amount *= gallons_per_quart * quarts_per_cup * cups_per_tablespoon

    # Convert the amount to the target unit
    if to_unit == "teaspoon":
        amount *= teaspoons_per_teaspoon
    elif to_unit == "cup":
        amount /= cups_per_tablespoon
    elif to_unit == "quart":
        amount /= quarts_per_cup
    elif to_unit == "gallon":
        amount /= gallons_per_quart

    # Return the converted amount
    return amount


convert_units(6, cup, teaspoon)
