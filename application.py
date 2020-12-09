import json
import flask
application = flask.Flask(__name__)

@application.route("/")
def get():
    return "Hello, world!"

