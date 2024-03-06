# This program converts kitchen measurements between tablespoons, teaspoons, cups, quarts, and gallons.

# Define the conversion factors.
tablespoons_per_teaspoon = 3
cups_per_tablespoon = 1 / 16
quarts_per_cup = 4 / 1
gallons_per_quart = 4 / 1

# Get the input from the user.
ingredient = input("Enter the ingredient you want to convert: ")
amount = float(input("Enter the amount you want to convert: "))
unit = input("Enter the unit of measurement you want to convert from: ")

# Convert the amount to tablespoons.
if unit == "teaspoons":
    amount = amount / tablespoons_per_teaspoon
elif unit == "cups":
    amount = amount * cups_per_tablespoon
elif unit == "quarts":
    amount = amount * quarts_per_cup * cups_per_tablespoon
elif unit == "gallons":
    amount = amount * gallons_per_quart * quarts_per_cup * cups_per_tablespoon

# Convert the amount to the desired unit.
if unit == "tablespoons":
    converted_amount = amount
elif unit == "teaspoons":
    converted_amount = amount * tablespoons_per_teaspoon
elif unit == "cups":
    converted_amount = amount / cups_per_tablespoon
elif unit == "quarts":
    converted_amount = amount / quarts_per_cup / cups_per_tablespoon
elif unit == "gallons":
    converted_amount = amount / gallons_per_quart / quarts_per_cup / cups_per_tablespoon

# Print the converted amount.
print(f"{amount} {unit} is equal to {converted_amount} tablespoons.")
