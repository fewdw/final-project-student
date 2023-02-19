from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import os
import io
import base64


smtp_email = os.environ.get("smtp_email")
smtp_password = os.environ.get("smtp_password")

def send_mail(employer_email, students):
    try:
        msg = f"""
        Dear Customer,

        We've attached the student information you requested to this email.

        If you have any questions or require further information, please feel free to contact us at isrsteam19@gmail.com.

        Thank you for your interest in our services.

        Sincerely,

        The ISRS Team
        """

        # Create the message object
        message = MIMEMultipart()
        message["from"] = "ISRS Team"
        message["to"] = employer_email
        message["subject"] = "Student Information from ISRS"

        # Attach the PDF for each student to the email message
        for student in students:
            name = student['name']
            pdf_data = base64.b64decode(student["resume"])
            pdf_stream = io.BytesIO(pdf_data)

            pdf_attachment = MIMEApplication(pdf_stream.read(), _subtype='pdf')
            pdf_attachment.add_header('Content-Disposition', 'attachment', filename=f'{name}-resume.pdf')
            message.attach(pdf_attachment)

        # Add the message body as text in the email body
        message.attach(MIMEText(msg))

        # Send the email using SMTP
        with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(smtp_email, smtp_password)
            smtp.send_message(message)
            return True
    except Exception as e:
        print(e)
        return False