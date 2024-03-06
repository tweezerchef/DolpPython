import pandas as pd
from tkinter import Tk, Entry, Frame, Listbox, END, Toplevel
from tkinter import ttk  # Import ttk module for styled widgets

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("/media/tom/Linux/Python/DolphinBasic/Data/SalesData.csv")

# Create a tkinter window
root = Tk()
root.title("Sales Data Viewer")
root.geometry("800x600")  # Set initial size of the window

# Styling options for ttk widgets
style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10))
style.configure("TFrame", background="#f0f0f0")

# Frame for input fields
input_frame = ttk.Frame(root)
input_frame.pack(pady=20)

# Create a label and text field for entering the customer name
ttk.Label(input_frame, text="Customer Name:").grid(row=0, column=0)
name_entry = Entry(input_frame)
name_entry.grid(row=0, column=1, padx=10)


# Function to clear the listbox selection and hide it
def clear_and_hide_listbox(listbox):
    listbox.delete(0, END)
    listbox.place_forget()


# Function to search for the customer data
def search_customer(*args):
    customer_name = name_entry.get()
    customer_data = df[df["Customer Name"] == customer_name]

    if not customer_data.empty:
        display_customer_data(customer_data)
    else:
        ttk.Label(root, text="No data found.", style="TLabel").pack()


# Function to display customer data in a modern table
def display_customer_data(customer_data):
    # Create a new window for displaying results
    results_window = Toplevel(root)
    results_window.title("Search Results")
    results_table = ttk.Treeview(
        results_window, columns=list(customer_data.columns), show="headings"
    )
    results_table.pack(fill="both", expand=True)

    # Configure column headers
    for col in customer_data.columns:
        results_table.heading(col, text=col)
        results_table.column(col, anchor="center")

    # Insert data into the table
    for _, row in customer_data.iterrows():
        results_table.insert("", "end", values=list(row))


# Autocomplete functionality for the text field
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


# Bind events for searching and autocompleting
name_entry.bind("<KeyRelease>", autocomplete)
root.bind("<Return>", search_customer)

# Create a search button
search_btn = ttk.Button(root, text="Search", command=search_customer)
search_btn.pack(pady=10)

root.mainloop()
