from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import os
import io
import base64


smtp_email = os.environ.get("smtp_email")
smtp_password = os.environ.get("smtp_password")

def send_mail(employer_email, student):
    try:
        print(student)
        msg = f"""
        Dear Customer,

        You have requested information from {student["first_name"]} {student["first_name"]},

        We have attached a PDF copy of the student's resume to this email. If you have any questions or require further information, please feel free to contact us at isrsteam19@gmail.com.

        Thank you for your interest in our services.

        Sincerely,

        The ISRS Team
        """


        # Create the message object
        message = MIMEMultipart()
        message["from"] = "ISRS Team"
        message["to"] = employer_email
        message["subject"] = "Student Information from ISRS"

        # Decode the base64-encoded PDF and create a stream
        pdf_data = base64.b64decode(student["resume"])
        pdf_stream = io.BytesIO(pdf_data)

        # Attach the PDF to the email message
        pdf_attachment = MIMEApplication(pdf_stream.read(), _subtype='pdf')
        pdf_attachment.add_header('Content-Disposition', 'attachment', filename='resume.pdf')
        message.attach(pdf_attachment)

        # Add the student data as text in the email body
        message.attach(MIMEText(msg))

        # Send the email using SMTP
        with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(smtp_email,smtp_password)
            smtp.send_message(message)
            return True
    except Exception as e:
        print(e)
        return False