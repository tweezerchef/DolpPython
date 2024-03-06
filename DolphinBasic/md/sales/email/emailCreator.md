### Introduction

I am a salesperson working for a large company that sells a wide variety of products. Recently, my company sent me a CSV file named `SalesData.csv`. My boss said I should use this data to improve my performance in 2024.

I opened the file up using Google Sheets and saw the columns `Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Discount`, `Profit`.

In each row is a record of every individual sale I closed, with the relevant information for that sale in the appropriate columns. The data begins in 2020 and goes all the way up to the present day in 2024. It looks like a lot of data, and I have no idea how to analyze it. I am not a technically inclined person, I don't know any programming languages, and I have never taken a math class beyond high school algebra.

I asked my friend in the IT department for help, and they recommended that I use the Python programming language to take the data and use it for analysis and other productivity enhancing tasks.

### Issue

I would like you to create a program, using Python that allows me to send an email to all the customers in the CSV file. Although the emails are not listed for the customers, they all have emails at my company's domain, `mycompany.com`.  The emails are simply their first and last names separated by a underscore with the company domain added after the last name. If there are any special characters in the name they are removed. Below are three examples with names taken from the `Customer Name` column in the CSV and the email version, that the program will have to create from those names.

| Customer Name | Email |
|---------------|-------|
| Philip Fox    | <Philip_Fox@mycompany.com>|
| John Stevensen | <John_Stevensen@mycompany.com>|
| Mary O'Conner | <Mary_OConner@mycompany.com>|

I would like to be able to have a simple interface that I can use with a window for typing or copy pasting my email and a button in the same window but outside the text box where the email's text will be entered.  When the button is pressed I want the email to be sent to all the customers in the `SalesData.csv`. The program needs to turn those names into their email, as illustrated above.  In addition there are duplicate names so the program needs to filter the duplicates so that only one email is sent to each unique customer.

### Summary of Program to Create

1. Create code in Python that allows me to send an email to all my customers email at the company domain `mycompany.com` using the `SalesData.csv` file for the customer names, and my email <sales_guru@mycompany.com> for the sender.  It will need to convert the names as they exist in the CSV file to the email format as shown in the table above.
2. The program should have a simple interface with a window for typing or copy pasting my email and a button to send the email to all the customers in the `SalesData.csv` file.
3. You may use any Python libraries you think are necessary to complete the task, but please make sure they are the most recent versions of the libraries you have access to.
4. Besides running the program (in VSCode) entering my email and pressing the button, the program should require no other actions from me to send the emails.
5. The program, in addition to sending the emails, should print a list of customers the email has been sent to.  This list should be printed to the console.
6. I am trying to learn Python and its libraries, so I would like the code to be well documented so I can understand how it works, in a manner that I can learn from and understand.
7. Once you have created this well documented code, return it to me as your response.
