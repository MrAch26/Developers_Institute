import flask
from flask import render_template, url_for, redirect

app = flask.Flask(__name__)


@app.route('/home')
def buildhome():
	#CONTROLLER:

	#MODEL:
	basket = ["apples", "oranges", "bananas"]
	show_items = True
	name = "Charlie"


	# VIEW
	if basket:
		return render_template('home.html', data = basket, show = show_items) #Flask automatically looks for templates in a folder called templates
	else:
		return redirect(url_for('sorrypage'))


@app.route('/products')
def products():
	return render_template('products.html')


@app.route('/sorry')
def sorrypage():
	#some logic here...
	return render_template('sorry.html')	


if __name__ == "__main__":
	app.run(debug=True)
