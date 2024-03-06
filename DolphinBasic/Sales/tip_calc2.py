# This function calculates the tip amount based on the pre-tax amount of the bill.
#
# Args:
#   total_bill: The total amount of the bill.
#   tax_rate: The local tax rate as a decimal.
#
# Returns:
#   The amount of money to tip.

def calculate_tip(total_bill, tax_rate):
    # Calculate the pre-tax amount of the bill.
    pre_tax_amount = total_bill / (1 + tax_rate)

    # Calculate the tip amount (20% of the pre-tax amount).
    tip_amount = pre_tax_amount * 0.2

    return tip_amount

# Get the total bill amount and tax rate from the user.
total_bill = float(input("Enter the total bill amount: "))
tax_rate = float(input("Enter the local tax rate as a decimal (e.g., 0.08): "))

# Calculate the tip amount.
tip_amount = calculate_tip(total_bill, tax_rate)

# Print the tip amount.
print(f"The tip amount is: ${tip_amount:.2f}")