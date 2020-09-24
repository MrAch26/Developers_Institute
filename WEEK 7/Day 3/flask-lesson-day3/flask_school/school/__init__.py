import flask

app = flask.Flask(__name__)

app.secret_key = "shalom"

from school import routes