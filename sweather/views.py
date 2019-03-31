from flask import render_template

from sweather import app


@app.route('/')
def index():
    pass

    
@app.route('/w')
def weather():
    return render_template('weather.html')
