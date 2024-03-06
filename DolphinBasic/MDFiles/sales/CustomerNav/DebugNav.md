### Introduction

I am a salesperson working for a large company that sells a wide variety of products. Recently, my company sent me a CSV file named `SalesData.csv`. My boss said I should use this data to improve my performance in 2024.

I opened the file up using Google Sheets and saw the columns `Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Discount`, `Profit`.

In each row is a record of every individual sale I closed, with the relevant information for that sale in the appropriate columns. The data begins in 2020 and goes all the way up to the present day in 2024. It looks like a lot of data, and I have no idea how to analyze it. I am not a technically inclined person, I don't know any programming languages, and I have never taken a math class beyond high school algebra.

I asked my friend in the IT department for help, and they recommended that I use the Python programming language to take the data and use it for analysis and other productivity-enhancing tasks.

### Program

Because of my technical incompetence, I don't know of a way to look for a customer and see all the sales information about them. I asked my friend in IT to make a program for me to do this, and I gave them specific requirements for the program.  Here is the program written in Python they created for me:

```Python
import pandas as pd
import tkinter as tk

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("/media/tom/Linux/Python/DolphinBasic/Data/SalesData.csv")

# Create a tkinter window
root = tk.Tk()
root.title("Sales Data Viewer")

# Create a label and text field for entering the customer name
tk.Label(root, text="Customer Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Create a function to search for the customer data
def search_customer():
    # Get the customer name from the text field
    customer_name = name_entry.get()

    # Search the DataFrame for rows where the Customer Name matches the input name
    customer_data = df[df["Customer Name"] == customer_name]

    # If no data is found, display a message
    if customer_data.empty:
        tk.Label(root, text="No data found.").grid(row=1, column=0, columnspan=2)
    else:
        # Create a table to display the customer data
        table = tk.Frame(root)
        table.grid(row=1, column=0, columnspan=2)

        # Create headers for the table
        for col in customer_data.columns:
            tk.Label(table, text=col).grid(
                row=0, column=customer_data.columns.get_loc(col)
            )

        # Add data to the table
        for i, row in customer_data.iterrows():
            for col in customer_data.columns:
                tk.Label(table, text=row[col]).grid(
                    row=i + 1, column=customer_data.columns.get_loc(col)
                )


# Create a search button
tk.Button(root, text="Search", command=search_customer).grid(row=0, column=2)

# Add autocomplete functionality to the text field
autocomplete_list = df["Customer Name"].unique().tolist()

def autocomplete(event):
    entry = event.widget
    text = entry.get()
    if text != "":
        matches = [name for name in autocomplete_list if name.startswith(text)]
        if matches:
            listbox = tk.Listbox(root)
            listbox.place(relx=0.25, rely=0.05)
            listbox.insert(0, *matches)
            listbox.bind(
                "<<ListboxSelect>>",
                lambda event: entry.delete(0, tk.END)
                and entry.insert(0, event.widget.get(event.widget.curselection())),
            )

name_entry.bind("<KeyRelease>", autocomplete)

# Run the tkinter main loop
root.mainloop()
```

### Issues With the Program

1. I had requested an "element and simple" design for the interface, but it is not elegant or stylish. I would like it to be more visually appealing.
2. The text field has an autocomplete feature, but when the `listbox` opens, there seems to be no way to select an item from the `listbox` and have it appear in the text field. The basic functionality of the autocomplete feature is working, but the final step of selecting an item from the `listbox` and having it appear in the text field is not working.
3. When a user hits the return key, the program should search for the customer name.  This is not happening.  I would like the program to search for the customer name when the return key is pressed as well as when the search button is pressed.
4. The window that first appears when running the program, is very small.  I would like the window to be larger when it first appears.  I would also like the box where the results will go, pre-rendered, and then the actual results to be placed in the box when the search is made.
5. When the results are returned, the table is not very visually appealing.  I want the table to have a more modern look and feel. Also, the table needs to be organized in a fashion that the user doesn't have to scroll horizontally to see all the data.  It needs to reorganize itself to fit in a standard-size window.
6. I would like the UI to have a more modern look and feel. If appropriate, I would like the program to use a more modern library to create the interface.
7. Please use your imagination to make the program more visually appealing and user-friendly. I want it to be a pleasure to use.

### Response

1. Please make all the changes listed above to the code, as well as any other changes you think are necessary to make the program more visually appealing and user-friendly.
2. Please remove the comments in the code above and add your own comments that explain your changes to the code.
3. Please then return to me the improved, newly commented, and debugged code as your response.
