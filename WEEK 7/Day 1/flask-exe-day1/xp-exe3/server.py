from flask import Flask,flash, render_template, request, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = b'hello_world'


@app.route('/')
def hello_world():  # this is a view
    return render_template('index.html')


@app.route('/random', methods=['GET', 'POST'])
def random_user():
    if request.method == "POST":
        user_number = request.form.get('user_input')
        return redirect(url_for('random100',number=user_number))
    return render_template('random_input.html')


@app.route('/random/<int:number>')
def random100(number):
    if number not in range(1, 101):
        flash("Number must be beetween 1 and 100")
        return redirect(url_for('random_user'))
    random_number = random.randint(1, 101)
    if number == random_number:
        return "SUCCESS the numbers are the same"
    return f"The number you chose is {number}, and the number we chose {random_number} "



def main():
    print('Running Server')
    app.run(debug=True)


if __name__ == '__main__':
    main()
