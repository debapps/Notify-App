import requests
import pandas as pd
from datetime import date
import os
from dotenv import load_dotenv

# This module gets the notification data from Google spreadsheet.

# Load the environment file.
load_dotenv()

class DataManager:
    # The Google Sheet URL.
    SHEET_URL = os.getenv('GOOGLE_SHEET_URL')


    def __init__(self):
        # Get the Google sheet data into DataFrame.
        response = requests.get(url=DataManager.SHEET_URL)
        response.raise_for_status()
        raw_data = response.json()
        notify_data = raw_data['notificationData']
        self.notify_df = pd.DataFrame(notify_data)

    @staticmethod
    def current_month():
        return date.today().month
    
    @staticmethod
    def current_day():
        return date.today().day

    def get_match_event(self):
        event = self.notify_df[(self.notify_df['month'] == DataManager.current_month()) &
                               (self.notify_df['day'] == DataManager.current_day())]
        
        if event.shape[0]:
            return event[['subject', 'content', 'emails']].to_dict(orient='records')
        else:
            return None
        

# data = DataManager()
# print(data.get_match_event())








