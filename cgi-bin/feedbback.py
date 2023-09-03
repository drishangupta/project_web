#!/usr/bin/python3
print("Content-type:text/html")
print()
import csv
import cgi
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

data = cgi.FieldStorage()
name1 = data.getvalue("name")
email1 = data.getvalue("email")
number1 = data.getvalue("number")
feedback1 = data.getvalue("feedback")

sender_email = 'minlinuxoth@gmail.com'
sender_password = 'eyhmddaiyhcxxyny'
recipient_email = email1

subject = "Feedback Confirmation"
message = f"Dear {name1},\n\nThank you for your feedback submission!"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    print("Confirmation email sent successfully.")
except Exception as e:
    print(f"Error sending email: {e}")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

feedback_data = {
    'Timestamp': [timestamp],
    'Name': [name1],
    'Email': [email1],
    'Number': [number1],
    'Feedback': [feedback1]
}

df = pd.DataFrame(feedback_data)

csv_file = 'feedback1.csv'
if not pd.io.common.file_exists(csv_file):
    df.to_csv(csv_file, index=False)
else:
    df.to_csv(csv_file, mode='a', header=False, index=False)

print("Feedback submitted and saved.")

