import flask
from flask import render_template

app = flask.Flask(__name__)

page = '''
<h1>Home</h1>
<h3>title</h3>
<p> Shalom</p>
'''


@app.route('/home')
def home():
    return '<h1>Welcome World</h1>'

@app.route('/index')
@app.route('/index/<name>')
def index(name='dada'):
    html = render_template('main_template.html', html_name=name)
    return html


if __name__ == "__main__":
    app.run(debug=True)
