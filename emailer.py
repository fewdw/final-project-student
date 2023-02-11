from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_mail(employer_email):
    try:
        message = MIMEMultipart()
        message["from"] = "ISRS Team"
        message["to"] = employer_email
        message["subject"] = "Student Information from ISRS"
        message.attach(MIMEText("Body"))

        with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("isrsteam19@gmail.com","enqxoehwrjwwnkdq")
            smtp.send_message(message)
            print("Sent!")
    except:
        print("Couldn't send email to ",employer_email)