import requests
import os
from dotenv import load_dotenv

# This module generates random quote.

# Load the environment file.
load_dotenv()

API_URL = os.getenv('QUOTE_URL')

def generate_quote():
    res = requests.get(API_URL)
    res.raise_for_status()
    data = res.json()
    return data['quote']

# print(generate_quote())


