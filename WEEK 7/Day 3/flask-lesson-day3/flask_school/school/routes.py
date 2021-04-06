from flask import render_template, flash, config
from school import app
from firebase_admin import credentials, firestore, initialize_app

# Use a service account
cred = credentials.Certificate(config('JSON_KEY1'))
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/")
def index():
    return "Working...<a href='/students'>ok</a>"

@app.route('/students')
def get_students():

    #Model - Get students from DB
    students = ["Adam", "Bob", "Charlie"]

    #View - render template
    html = render_template('students.html', students=students)

    flash('Flashhhh Message', "Flash")
    flash("You logged in very well", "green")
    flash("Your Wifi is not working :(", "red")
    return html