import smtplib
import ssl
from email.message import EmailMessage
from email import password

subject = "sending email from python"
body = "This is to test sending the email using python"
sender_email = "area0xx@gmail.com"
receiver_email = "woyac14709@ishyp.com"
password = password

message = EmailMessage()
message["from"] = sender_email
message["to"] = receiver_email
message["subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("sending email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context)as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")










