### Introduction

I am a salesperson working for a large company that sells a wide variety of products. Recently, my company sent me a CSV file called `SalesData.csv`. My boss said I should use this data to improve my performance in 2024.

I opened the file up using Google Sheets and saw the columns `Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Discount`, `Profit`.

In each row is a record of every individual sale I closed, with the relevant information for that sale in the appropriate columns. The data begins in 2020 and goes all the way up to the present day in 2024. It looks like a lot of data, and I have no idea how to analyze it. I am not a technically inclined person, I don't know any programming languages, and I have never taken a math class beyond high school algebra.

I asked my friend in the IT department for help, and they recommended that I use the Python programming language to take the data and use it for analysis or other productivity-enhancing tools.

### Issue

 I have a very hard time recommending products to customers. Because I don't make a lot of sales to repeat customers, this makes it even more difficult to predict what to recomend, however I was thinking that maybe the states that the customers order from could be a good indicator of what they might like if combined with each clients purchase history. I asked my friend in the IT department for help, and they said that collaborative filtering could be a good way to go about this. The problem is I have no idea what that is or how to do it.

### Task

I need you to create code that will take the data from the `SalesData.csv` file and use it to recommend products to customers based on their purchase history and the purchase history of customers in their state.  I would then like to be able to enter as an input a customer name or state.  The program should then output a list of recommended products for that customer or state based on its analysis of the data.  The program should also output the model score for the recommendation engine.  I have included some of the details below but feel free to use your imagination to best implement a solution.

### Summary Of Code to Create

1. Code should be written in Python. You may use any libraries you see fit; however, `pandas` and `scikit-learn` were suggested to me.
2. The code should read the `SalesData.csv` file and use it to recommend products to customers based on their purchase history and the purchase history of customers in their state. Use the collaborative filtering method to identify products to recommend.
3. When the code is run, it should prompt the user to enter a customer name or state.
4. The code should then output a list of recommended products for that customer or state.
5. The code should also output the model score for the recommendation engine.
6. The code you generate does not need extensive documentation, but you should include comments to explain what it is doing.
