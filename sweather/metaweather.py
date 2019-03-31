# https://www.metaweather.com/api/
import requests


API_URL = 'https://www.metaweather.com/api'


def search(city):
    req = requests.get("{api_url}/location/search/?query={city}".format(
                api_url=API_URL, city=city))
    if req.status_code != 200:
        return (0, 'API returned'+req.status_code)
    else:
        return req.json()

