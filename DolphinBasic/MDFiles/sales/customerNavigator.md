### Introduction

I am a salesperson working for a large company that sells a wide variety of products. Recently, my company sent me a CSV file named `SalesData.csv`. My boss said I should use this data to improve my performance in 2024.

I opened the file up using Google Sheets and saw the columns `Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Discount`, `Profit`.

In each row is a record of every individual sale I closed, with the relevant information for that sale in the appropriate columns. The data begins in 2020 and goes all the way up to the present day in 2024. It looks like a lot of data, and I have no idea how to analyze it. I am not a technically inclined person, I don't know any programming languages, and I have never taken a math class beyond high school algebra.

I asked my friend in the IT department for help, and they recommended that I use the Python programming language to take the data and use it for analysis and other productivity enhancing tasks.

### Issue

Because of my technical incompetence, I don't know of a way to look for a customer and see all the sales information about them.  I would like you to make a program using Python that allows me to do this.

### Summary of Program to Create

1. Written in Python using commonly used libraries.
2. Uses the `SalesData.csv` file for the information I need to see and the customers I am searching for.
3. I am very into aesthetics so I would like the program to have a simple yet elegant interface.
4. The interface should have three main components: a text field for typing in customer names, a search button, and a display area for the relevant sales information.
5. The interface should have a text box at the top for typing in customer names. This text box should also use a simple search algorithm (or a library) to find the customer names as I type them in and suggest completions for them. The suggestions should be the names in the `Customer Name` column of the `SalesData.csv` file.
6. The interface should have a search button, next to the text box that, when pressed, will take the name in the text box and search the `SalesData.csv` file for all sales data associated with that customer's name. If the name is not found or there is no sales data for that customer, the program should display a message along the lines of "No Data Found."  If the name is found, the program should display all the sales information for that customer in a table in the display area.
7. You do not need to document the code heavily; please just make sure it is clean and well organized.
8. Once you have created this code, return it to me as your response.
