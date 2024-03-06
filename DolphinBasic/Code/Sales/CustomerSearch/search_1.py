import pandas as pd
import tkinter as tk

# Load the sales data from the CSV file
df = pd.read_csv("/media/tom/Linux/Python/DolphinBasic/Data/SalesData.csv")

# Create the main window
window = tk.Tk()
window.title("Sales Data Search")

# Create the text field for entering customer names
name_label = tk.Label(window, text="Customer Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()


# Create the search button
def search_data():
    # Get the customer name from the text field
    customer_name = name_entry.get()

    # Search for the customer's sales data
    customer_data = df[df["Customer Name"] == customer_name]

    # Check if any data was found
    if customer_data.empty:
        results_label["text"] = "No Data Found."
    else:
        # Display the results in a table
        results_label["text"] = customer_data


search_button = tk.Button(window, text="Search", command=search_data)
search_button.pack()

# Create the display area for the results
results_label = tk.Label(window, text="")
results_label.pack()

# Run the main loop
window.mainloop()
