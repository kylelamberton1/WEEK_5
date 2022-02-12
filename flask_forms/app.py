from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = '2468'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    dob = DateField('dob')
    favourite_number = IntegerField('Favourite Number')
    favourite_food = SelectField('Favourite Food', choices=[('pizza', 'PIZZA'),('spaghetti', 'SPAGHETTI'), ('chilli', 'CHILLI')])
    submit = SubmitField('Add Details')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        favourite_number = form.favourite_number.data
        favourite_food = form.favourite_food.data


        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {first_name} {last_name}. Your username is: {dob}{favourite_number}{favourite_food}'

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')