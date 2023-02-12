from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

smtp_email = os.environ.get("smtp_email")
smtp_password = os.environ.get("smtp_password")

def send_mail(employer_email,student):

    message = " "

    try:
        message = MIMEMultipart()
        message["from"] = "ISRS Team"
        message["to"] = employer_email
        message["subject"] = "Student Information from ISRS"
        message.attach(MIMEText(str(student)))

        with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(smtp_email,smtp_password)
            smtp.send_message(message)
            return True
    except:
        return False