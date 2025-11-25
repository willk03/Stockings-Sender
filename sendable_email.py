"""Object to send email"""

import smtplib
from email.message import EmailMessage

class SendableEmail:
    """Email object"""

    def __init__(self, 
                 sender_email: str, 
                 password: str, 
                 recipient_email: str, 
                 subject: str, 
                 body: str
                 ):
        self._sender_email: str = sender_email
        self._password: str = password
        self.recipient_email: str = recipient_email
        self.subject: str = subject
        self.body: str = body

    def send(self) -> None:
        """Send emaiil"""
        message = EmailMessage()
        message.set_content(self.body)
        message["From"] = self._sender_email
        message["To"] = self.recipient_email
        message["Subject"] = self.subject

        server = "smtp.gmail.com" # Example for Gmail
        port = 465 # SSL port for secure connection Use 587 for TLS

        try:
            # Connect to the SMTP server (using Gmail as an example)
            # For other providers, you'll need their specific SMTP server and port
            smtp_server = smtplib.SMTP_SSL(server, port)
            smtp_server.login(self._sender_email, self._password)

            # Send the email
            smtp_server.sendmail(self._sender_email, self.recipient_email, message.as_string())
            print("Email sent successfully!")

        except Exception as e:
            print(f"Error sending email: {e}")

        finally:
            # Close the SMTP connection
            if 'smtp_server' in locals() and smtp_server:
                smtp_server.quit()


email = SendableEmail(
    sender_email='will.kuster6@gmail.com',
    password='cipk koqa ghcj glqo',
    recipient_email='jasonmonaco@icloud.com',
    subject='Test',
    body='Hi queen\n- Will'
)

import random
for i in range(100):
    email.subject = f'There are {random.randint(50, 5000)} HOT singles in your area!!!'
    email.send()
