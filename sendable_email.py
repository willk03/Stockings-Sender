"""Object to send email"""

import smtplib
from email.message import EmailMessage
from typing import Optional

class SendableEmail:
    """Email object"""

    def __init__(self,
                 recipient_email: str,
                 sender_email: Optional[str] = None,
                 password: Optional[str] = None
                 ):
        self._sender_email: Optional[str] = sender_email
        self._password: Optional[str] = password
        self.recipient_email: str = recipient_email
        self.subject: Optional[str] = None
        self.body: Optional[str] = None

    def send(self) -> None:
        """Send emaiil"""
        if self._sender_email is None or self._password is None:
            raise ValueError("Must enter sender email and password before sending.")
        if self.subject is None or self.body is None:
            raise ValueError("Must set subject and body before sending.")
        message = EmailMessage()
        message.set_content(self.body)
        message["From"] = self._sender_email
        message["To"] = self.recipient_email
        message["Subject"] = self.subject

        server = "smtp.gmail.com"
        port = 465 # SSL port for secure connection Use 587 for TLS

        try:
            smtp_server = smtplib.SMTP_SSL(server, port)
            smtp_server.login(self._sender_email, self._password)
            smtp_server.sendmail(self._sender_email, self.recipient_email, message.as_string())
            print("Email sent successfully!")

        except Exception as e:
            print(f"Error sending email: {e}")

        finally:
            # Close the SMTP connection
            if 'smtp_server' in locals() and smtp_server:
                smtp_server.quit()

    def login_from_file(self, filename: str) -> None:
        """Login from file containing gemail/app password"""
        with open(filename, 'r') as data:
            login_info = data.readlines()
            self._sender_email = login_info[0]
            self._password = login_info[1]

    def set_subject(self, subject: str) -> None:
        """Set the subject of the email"""
        self.subject = subject

    def set_body(self, body: str) -> None:
        """Set the subject of the email"""
        self.body = body
