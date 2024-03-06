import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("/media/tom/Linux/Python/DolphinBasic/Sales/SalesData.csv")


# Function to convert customer names to email addresses
def create_email(name):
    # Remove special characters and convert to lowercase
    name = name.replace(" ", "_").replace("'", "").replace("-", "").lower()
    # Create the email address
    return f"{name}@mycompany.com"


# Create a set of unique customer names
unique_customers = df["Customer Name"].unique()

# Create a list of email addresses
email_addresses = [create_email(name) for name in unique_customers]

# Email credentials
sender_email = "sales_guru@mycompany.com"
password = "your_password"


# Create a function to send the emails
def send_emails(email_body):
    # Create a message object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = "Subject of your email"
    message.attach(MIMEText(email_body, "plain"))

    # Create an SMTP server instance
    server = smtplib.SMTP(
        "smtp.mycompany.com", 587
    )  # Replace with your company's SMTP server address and port
    server.starttls()
    server.login(sender_email, password)

    # Send the emails
    for email_address in email_addresses:
        message["To"] = email_address
        server.sendmail(sender_email, email_address, message.as_string())

    # Close the server connection
    server.quit()


# Print a list of customers to whom the email has been sent
print("Email sent to the following customers:")
for name in unique_customers:
    print(name)

# Create a simple GUI with a text box and a button


class EmailSenderApp:
    def __init__(self, master):
        self.master = master
        master.title("Email Sender")

        # Create a text box for the email body
        self.email_body_text = tk.Text(master)
        self.email_body_text.pack()

        # Create a button to send the emails
        self.send_button = tk.Button(
            master, text="Send Emails", command=self.send_emails
        )
        self.send_button.pack()

    def send_emails(self):
        email_body = self.email_body_text.get("1.0", "end-1c")
        send_emails(email_body)


# Create the GUI and run it
root = tk.Tk()
app = EmailSenderApp(root)
root.mainloop()
