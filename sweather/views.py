from sweather import app

@app.route('/')
def index():
    return 'works'

