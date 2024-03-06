import pandas as pd
import smtplib
import re
from email.message import EmailMessage

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("SalesData.csv")

# Remove duplicate customer names
unique_customers = df["Customer Name"].unique()


# Function to convert customer names to email addresses
def create_email(customer_name):
    # Remove special characters
    name = re.sub("[^A-Za-z]", "", customer_name)

    # Split the name into first and last names
    first_name, last_name = name.split()

    # Create the email address
    email = f"{first_name}_{last_name}@mycompany.com"

    return email


# Create a list of customer email addresses
customer_emails = [create_email(name) for name in unique_customers]

# Create the email message
msg = EmailMessage()
msg["From"] = "sales_guru@mycompany.com"
msg["Subject"] = "Important Announcement"

# Add the email body (replace with your desired message)
msg.set_content(
    "Dear Valued Customer, \n\nWe hope this email finds you well. \n\nThank you for your continued support.\n\nSincerely,\nThe Sales Team"
)

# Connect to the SMTP server
server = smtplib.SMTP("smtp.mycompany.com")

# Send the email to each customer
for email in customer_emails:
    msg["To"] = email
    server.send_message(msg)
    print(f"Email sent to: {email}")

# Disconnect from the SMTP server
server.quit()
