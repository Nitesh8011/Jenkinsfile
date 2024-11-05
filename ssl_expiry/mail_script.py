import smtplib
import os
from email.mime.text import MIMEText


def send_email(subject, message, to_email):
    from_email = os.environ.get('FROM_EMAIL')
    password = os.environ.get('SMTP_PASSWORD')

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
