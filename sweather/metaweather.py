# https://www.metaweather.com/api/
import requests


API_URL = 'https://www.metaweather.com/api'


def search(city):
    req = requests.get("{api_url}/location/search/?query={city}".format(
                api_url=API_URL, city=city))
    return req.json()


def get_woeid(city):
    city_list = search(city)
    return city_list[0]['woeid']


def get_weather(woeid):
    req = requests.get("{api_url}/api/location/{woeid}".format(
                api_url=API_URL, woeid=woeid.decode("UTF-8")))
    return req.json()['consolidated_weather']
