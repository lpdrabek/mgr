from flask import render_template, request
import json

from pprint import pprint

from sweather import app
from sweather.metaweather import search


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/city_select')
def weather():
    cities = request.args.get('cities')
    if not cities:
        return render_template('skel.html')
    c_list = cities.split('\r\n')
    all_cities = {}
    for city in c_list:
        a = search(city)
        print(a[0]['title'])
        all_cities[city] = search(city)
    pprint(all_cities)
    return render_template('weather.html', cities=all_cities)


@app.route('/weather')
def index():
    return render_template('index.html')
