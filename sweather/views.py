from os import environ

from flask import render_template, request, abort
import redis

from sweather import app
from sweather.metaweather import get_weather
from sweather.lib import populate_cache

DEF_CITIES = ['Warsaw', 'London', 'Berlin']


@app.route('/')
def index():
    r = redis.Redis(host=environ.get('REDIS_HOST', 'localhost'), port=6379)
    populate_cache(r, DEF_CITIES)

    city = request.args.get('city', 'warsaw')
    woeid = r.hget('cities', city.lower())
    if not woeid:
        abort(404)

    weather = get_weather(woeid)

    return render_template('index.html', weather=weather, cities=DEF_CITIES)
