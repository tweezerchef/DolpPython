
def calculate_tip(total_bill, tax_rate):

    tax_amount = total_bill * tax_rate

    pre_tax_amount = total_bill - tax_amount

    tip_amount = pre_tax_amount * 0.20

    return tip_amount


total_bill = float(input("Enter the total bill amount: "))
tax_rate = float(input("Enter the local tax rate as a decimal (e.g., 0.08): "))

tip_amount = calculate_tip(total_bill, tax_rate)


print(f"The tip amount is: ${tip_amount:.2f}")
