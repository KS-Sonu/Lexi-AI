import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_email(to_email, subject, message):
    from_email = os.getenv("GMAIL_EMAIL")
    app_password = os.getenv("GMAIL_APP_PASSWORD")  # Use App Password, not your real Gmail password

    try:
        # Clean any non-UTF8 characters
        message = message.encode('utf-8', 'ignore').decode('utf-8')

        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject

        # Attach the cleaned message with UTF-8 encoding
        body = MIMEText(message, "plain", "utf-8")
        msg.attach(body)

        # Connect and send email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, app_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
