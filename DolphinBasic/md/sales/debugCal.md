### Introduction

I am a businessperson who works in sales.  Very often, I must take potential clients out on the town, and we typically end up at a bar.  However, I have a problem with calculating the tip on the bill when we go out to a bar.

An issue arises because I have a company credit card that I use to pay for clients entertainment amd my company has some rather arcane rules regarding tips.  We are required to tip 20%, but only on the pre-tax amount of any bill.  This is a problem because, unlike with restaurants, sales tax is built into the menu price of the drink at a bar, and I need to be able to calculate the tip based on the pre-tax amount of the bill.

### First Solution

I contacted my buddy in IT, and they just sent me this Python file to help me calculate the tip.  The contents of the file are as follows:

```Python
def calculate_tip(total_bill, tax_rate):

    tax_amount = total_bill * tax_rate

    pre_tax_amount = total_bill - tax_amount

    tip_amount = pre_tax_amount * 0.20

    return tip_amount


total_bill = float(input("Enter the total bill amount: "))
tax_rate = float(input("Enter the local tax rate as a decimal (e.g., 0.08): "))

tip_amount = calculate_tip(total_bill, tax_rate)


print(f"The tip amount is: ${tip_amount:.2f}")
```

#### Problem

I figured out a way to get this up and running on the laptop I bring to all sales meetings.  The current client I am working with is an expert mathematician, and I wanted to show off my new fancy tool. So I used it to calculate the tip on a $100 bill with a 8% tax rate.  I was so proud of myself, but then the client told me that the tip was wrong.  I was so embarrassed.

I double checked the math on my calculator and my client was right.  Here is a table of the inputs, the correct tip amount and the tip amount my program calculated:

| Total Bill | Tax Rate | Correct Tip Amount | Program's Tip Amount |
|------------|----------|---------------------|----------------------|
| $100.00    | 8%      | $18.52              | $18.40               |
| $500.00   | 6%     | $94.34             | $94.00              |

While these differences may seem small, my company is so strict I may get fired for these small discrepancies.

#### What I Need You To Do

1. Please debug this code so that the expected/correct tip amount is the programs output for any given input.
2. Please also explain to me what you have changed, in bullet point format, in a way I can easily understand. Please explain any additional points about the code I need to understand in the context of these changes.
3. Remember, I am not a programer and I don't know what any computer science term is. For example, my friend explained that this code contains a function, but I have no idea what a function is.  Please do not use any term like that.  Use terms a high school freshman would understand.
4. Please give me some sample inputs and correct outputs so I can test the program to ensure it works.  Please give me at least three different inputs and the correct outputs for those inputs.
5. Return these three requests for me in the following format
    * First, the explanation of the changes you made to the code in a bullet point list.
    * Second, the corrected code, with the changes you made.
    * Third, the sample inputs and the correct outputs for those inputs in table format.
