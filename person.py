"""Data structure for person to store email and name"""

from typing import Optional
from sendable_email import SendableEmail

class Person:
    """
    Stores the person and who they have for their stocking
    Also creates an email object to send
    """

    def __init__(self, name: str, email: str, login_file: str) -> None:
        self.name: str = name
        self.target: Optional[str] = None
        self.email: SendableEmail = SendableEmail(email)
        self.email.login_from_file(login_file)

    def set_target(self, name: str) -> None:
        """Sets the target and email recipient"""
        self.target = name
        self.email.set_subject('Stocking!!!!!')
        self.email.set_body(f'Your stocking target is {name}! Have fun shopping!!')

    def send_email(self) -> None:
        """Sends email"""
        self.email.send()

    def __str__(self) -> str:
        return self.name
