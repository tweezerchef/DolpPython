import pandas as pd
import tkinter as tk
from tkinter import ttk

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("/media/tom/Linux/Python/DolphinBasic/Data/SalesData.csv")

# Create a tkinter window with a modern style
root = tk.Tk()
root.title("Sales Data Viewer")
ttk.Style().theme_use("clam")


# Set the initial window size
root.geometry("1000x600")

# Create a container frame for the search and results sections
container = ttk.Frame(root)
container.pack(fill="both", expand=True)

# Create a search section
search_frame = ttk.Frame(container)
search_frame.pack(side="top", fill="x", padx=20, pady=10)

# Create a label and text field for entering the customer name
ttk.Label(search_frame, text="Customer Name:").grid(row=0, column=0)
name_entry = ttk.Entry(search_frame)
name_entry.grid(row=0, column=1)

# Create a results section
results_frame = ttk.Frame(container)
results_frame.pack(side="bottom", fill="both", expand=True, padx=20, pady=10)


# Create a function to search for the customer data
def search_customer():
    # Get the customer name from the text field
    customer_name = name_entry.get()

    # Search the DataFrame for rows where the Customer Name matches the input name
    customer_data = df[df["Customer Name"] == customer_name]

    # If no data is found, display a message
    if customer_data.empty:
        ttk.Label(results_frame, text="No data found.").pack(pady=10)
    else:
        # Create a table to display the customer data
        table = ttk.Treeview(results_frame)

        # Set up the table columns and headings
        table["columns"] = list(customer_data.columns)
        for col in customer_data.columns:
            table.heading(col, text=col)

        # Add data to the table
        for i, row in customer_data.iterrows():
            table.insert("", tk.END, values=list(row))

        # Pack the table in the results section
        table.pack(fill="both", expand=True)


# Create a search button
ttk.Button(search_frame, text="Search", command=search_customer).grid(row=0, column=2)

# Add autocomplete functionality to the text field
autocomplete_list = df["Customer Name"].unique().tolist()


def autocomplete(event):
    text = name_entry.get()
    if text:
        matches = [
            name for name in df["Customer Name"].unique() if name.startswith(text)
        ]
        if matches:
            autocomplete_listbox = Listbox(root, height=4)
            autocomplete_listbox.place(relx=0.25, rely=0.05)
            for match in matches:
                autocomplete_listbox.insert(END, match)

            def on_select(event):
                name_entry.delete(0, END)
                name_entry.insert(
                    0, autocomplete_listbox.get(autocomplete_listbox.curselection())
                )
                clear_and_hide_listbox(autocomplete_listbox)

            autocomplete_listbox.bind("<<ListboxSelect>>", on_select)


def select_from_listbox(event):
    search_customer()


name_entry.bind("<KeyRelease>", autocomplete)
name_entry.bind("<Return>", select_from_listbox)

# Run the tkinter main loop
root.mainloop()
