from smtplib import SMTP
from os import getenv
from typing import List, Optional

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self) -> None:
        self.server = SMTP(
            host = getenv('SMTP_HOSTNAME'),
            port = getenv('SMTP_TLS_PROT')
        )
    def connect_server(self):
        self.server.starttls()
        self.server.login(
            user=getenv('SMTP_USER'),
            password=getenv('SMTP_PASSWORD')
        )

    def send_email(self, emails: List[str], subject: Optional[str], **kwargs):
        self.connect_server()
        print('Sending email . . .')
        for email in emails:
            mime = MIMEMultipart()
            mime['From'] = getenv('SMTP_USER')
            mime['To'] = email
            mime['SUbject'] = subject
            format = MIMEText(kwargs['message_format'], kwargs['format'])
            mime.attach(format)
            try:
                self.server.sendmail(getenv('SMTP_USER'), email, mime.as_string())

            except Exception as e:
                raise e
            finally:
                self.disconnet_server()

    def disconnet_server(self):
        self.server.quit()
        self.server.close()
    