import datetime
import requests

def get_fact():
    """
    Get a random fact from https://history.muffinlabs.com/date
    """

    url = 'http://history.muffinlabs.com/date'
    response = requests.get(url)
    data = response.json()
    return data

