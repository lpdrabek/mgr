import flask

import sweather

app = flask.Flask(__name__)

with app.test_request_context('/'):
    assert flask.request.path == '/'
    assert sweather.views.index() == 'works'

