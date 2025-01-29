import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

# This module generates random quote.

# Load the environment file.
load_dotenv()

# Get the environment variables and constants.
QUOTE_URL = os.getenv('QUOTE_API_URL')
NEWS_URL = os.getenv('NEWS_API_URL')
NEWS_KEY = os.getenv('NEWS_API_KEY')
NEWS_TOPIC = os.getenv('NEWS_TOPIC')

def get_api_call(url, params = None):
    '''This function returns get api call results.'''
    res = requests.get(url, params)
    res.raise_for_status()
    data = res.json()
    return data

def generate_quote():
    '''This Function generates random quotes.'''

    data = get_api_call(QUOTE_URL)
    return data['quote']

def get_prev_date():
    '''This Function generates previous date in string format.'''

    # Get today's date
    today = datetime.now()
    # Calculate the previous date
    previous_date = today - timedelta(days=1)
    # Format the previous date as a string
    previous_date_str = previous_date.strftime('%Y-%m-%d')
    return previous_date_str

def generate_news_HTML():
    '''This Function generates the News content.'''
    parameters = {
        'q': NEWS_TOPIC,
        'language': 'en',
        'sortBy': 'popularity',
        'pageSize': '5',
        'from': get_prev_date(),
        'apiKey': NEWS_KEY
    }

    # Get the News items from API.
    data = get_api_call(NEWS_URL, params=parameters)

    # Format News Data
    news_articles = [{
        "title": news['title'], 
        "desc": news['description'],
        "url": news['url'],
        'image': news['urlToImage'],
        'source': news['source']['name']
        } for news in data['articles']]
    
    # Get the HTML News template.
    try:
        with open(os.path.join('emails', 'news_temp.html'), 'r') as news_temp_file:
            news_temp = news_temp_file.read()
    except FileNotFoundError:
        email_path = os.getenv('ABS_PATH')
        with open(os.path.join(email_path, 'news_temp.html'), 'r') as news_temp_file:
            news_temp = news_temp_file.read()

    # Generate News content.
    news_content = ''
    for item in news_articles:
        news_content += news_temp.format(source=item['source'], 
                                         title=item['title'],
                                         img_url=item['image'],
                                         content=item['desc'],
                                         news_url=item['url'])
    return news_content
