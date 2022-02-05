import requests
import os
from dotenv import load_dotenv
import datetime
load_dotenv()

def get_news_articles(query):
    """
    Get news articles matching a query
    """
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    url = ('https://newsapi.org/v2/everything?'+
           f'q={query}&'+
           'from={}&'.format((datetime.datetime.now().strftime('%Y-%m-%d')))+
           'apiKey=' + NEWS_API_KEY)
    response = requests.get(url)
    return response.json()['articles']

