import os
from dotenv import load_dotenv

# This module generates random quote.

# Load the environment file.
load_dotenv()

class DailyEmail:
    IMAGE = os.getenv('IMG_URL')

    def __init__(self, quote):
        self.q = quote
        content = f'<article><img src="{DailyEmail.IMAGE}"/><h3>Good Morning Debaditya!</h3><h5>The Quote of the Day... </h5><p>"{self.q}"</p></article>'
        subject = 'Greetings for the day...' 
        self.email = (subject, content)

    def get_email(self):
        return self.email
