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
