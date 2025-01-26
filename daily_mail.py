import os
from dotenv import load_dotenv

# This module generates random quote.

# Load the environment file.
load_dotenv()

class DailyEmail:
    IMAGE = os.getenv('IMG_URL')

    def __init__(self, quote, news):
        subject = 'Greetings for the day...' 
        with open('email_content/daily_email_content.html', 'r') as content_file:
            raw_content = content_file.read()
            content = raw_content.format(image_var = DailyEmail.IMAGE, 
                                         quote_var = quote,
                                         news_var = news) 
        self.email = (subject, content)

    def get_email(self):
        return self.email
