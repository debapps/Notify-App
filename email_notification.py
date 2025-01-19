import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# This Module sends emails to multiple recipients.

# Load the environment file.
load_dotenv()

class EmailNotify:
    # Class variables.
    # Email account credentials.
    MAIL_HOST = 'smtp.gmail.com'
    MAIL_PORT = 587
    APP_PASS = os.getenv('APP_PASS_CODE')
    FROM_EMAIL = 'bhar.debaditya@gmail.com'

    def __init__(self, to_emails, subject, content, is_html = False):
        # MIME Setup.
        self.msg = MIMEMultipart()
        self.msg['From'] = EmailNotify.FROM_EMAIL
        self.msg['To'] = ','.join(to_emails)
        self.msg['Subject'] = subject
        
        # Setting email body.
        if is_html:
            self.msg_type = 'html'
        else:
            self.msg_type = 'plain'
        self.msg.attach(MIMEText(content, self.msg_type))

    def send_email(self):
        '''This function sends the emails.'''
        try:
            with smtplib.SMTP(EmailNotify.MAIL_HOST, EmailNotify.MAIL_PORT) as self.server:
                self.server.starttls()
                self.server.login(EmailNotify.FROM_EMAIL, EmailNotify.APP_PASS)
                self.server.sendmail(EmailNotify.FROM_EMAIL, self.msg['To'].split(','), 
                                     self.msg.as_string())
                print('Email sent successfully.')
        except Exception as ex:
            print(ex)


# # to_emails = ['debaditya.bhar@gmail.com', 'debadityabhar@icloud.com', 'debaditya.bhar@outlook.com']
# to_emails = ['debaditya.bhar@gmail.com']
# body = '''
# <html><body>
# <h2>Hello World!</h2>
# <p>This email you received from python code.</p>
# </html></body>
# '''
# # body = 'Hello World!\nThis email you received from python code.'

# en = EmailNotify(to_emails, 'Hello Python!', body, True)
# en.send_email()
