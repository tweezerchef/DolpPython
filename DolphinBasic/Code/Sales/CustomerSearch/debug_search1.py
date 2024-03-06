import pandas as pd
import tkinter as tk
from tkinter import ttk

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("/media/tom/Linux/Python/DolphinBasic/Data/SalesData.csv")

# Create a tkinter window with a modern style
root = tk.Tk()
root.title("Sales Data Viewer")
root.style = ttk.Style()
root.style.theme_use("clam")

# Set the initial window size
root.geometry("1200x600")

# Create a frame for the search functionality
search_frame = ttk.Frame(root)
search_frame.pack(pady=20)

# Create a label and text field for entering the customer name
ttk.Label(search_frame, text="Customer Name:").grid(row=0, column=0, padx=10)
name_entry = ttk.Entry(search_frame)
name_entry.grid(row=0, column=1, padx=10)


# Create a function to search for the customer data
def search_customer():
    # Get the customer name from the text field
    customer_name = name_entry.get()

    # Search the DataFrame for rows where the Customer Name matches the input name
    customer_data = df[df["Customer Name"] == customer_name]

    # If no data is found, display a message
    if customer_data.empty:
        result_label = ttk.Label(result_frame, text="No data found.")
        result_label.grid(row=0, column=0, columnspan=2)
    else:
        # Remove any previous results
        for widget in result_frame.winfo_children():
            widget.destroy()

        # Create a table to display the customer data
        table = ttk.Treeview(result_frame, columns=customer_data.columns)
        table.grid(row=1, column=0, columnspan=2)

        # Add headers to the table
        for col in customer_data.columns:
            table.heading(col, text=col)

        # Add data to the table
        for i, row in customer_data.iterrows():
            table.insert("", tk.END, values=row)

        # Adjust column widths to fit the data
        for col in customer_data.columns:
            table.column(
                col, width=len(max(customer_data[col].astype(str), key=len)) * 10
            )


# Create a search button
ttk.Button(search_frame, text="Search", command=search_customer).grid(
    row=0, column=2, padx=10
)

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

# Bind the search function to the Return key
root.bind("<Return>", lambda event: search_customer())

# Create a frame for the results
result_frame = ttk.Frame(root)
result_frame.pack(fill=tk.BOTH, expand=True)

# Run the tkinter main loop
root.mainloop()
