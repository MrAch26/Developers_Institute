import random
from flask import render_template_string, render_template
from colors import app, database



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/square')
def square():
    data = database.load_database('color_db.json')
    template_file = open('colors/templates/square.html', 'r').read()

    random_color = random.choice(data['colors'])
    random_color = random_color['color']


    return render_template_string(template_file, color=random_color)



@app.route('/triangle')
def triangle():
    data = database.load_database('color_db.json')
    template_file = open('colors/templates/triangle.html', 'r').read()

    random_color = random.choice(data['colors'])
    random_color = random_color['color']

    return render_template_string(template_file, color=random_color)


@app.route('/circle')
def circle():
    data = database.load_database('color_db.json')
    template_file = open('colors/templates/circle.html', 'r').read()

    random_color = random.choice(data['colors'])
    random_color = random_color['color']

    return render_template_string(template_file, color=random_color)
