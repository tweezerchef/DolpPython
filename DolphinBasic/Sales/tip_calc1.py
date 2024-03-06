def calculate_tip(total_bill, tax_rate):

    pre_tax_amount = total_bill / (1 + tax_rate)

    tip = pre_tax_amount * 0.20

    return tip

total_bill = float(input("Enter the total amount of the bill: "))
tax_rate = float(input("Enter the local tax rate as a decimal: "))

tip = calculate_tip(total_bill, tax_rate)

print("The tip amount is:", tip)