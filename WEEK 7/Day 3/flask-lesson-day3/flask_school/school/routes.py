from flask import render_template, flash
from school import app

@app.route("/")
def index():
    return "Working..."

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