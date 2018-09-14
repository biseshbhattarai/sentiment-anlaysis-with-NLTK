from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, flash, redirect, request, abort
# from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, TextAreaField, Form
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import sentiment_mod as s

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    data = db.Column(db.String(10000))

    def __repr__ (self):
        return self.name


@app.route("/")
def home():
    return render_template('home.html')

class TestForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=200)])
    data = TextAreaField('Please enter the text here', [validators.Length(max=300000)])



@app.route('/form', methods=['POST', 'GET'])
def getform():
    form = TestForm(request.form)

    if request.method == 'POST' and form.validate():
        test = Test(name=form.name.data, data=form.data.data)
        data = form.data.data
        # flash('Success ! , Wait for a while dude', 'success')
        
        print(s.sentiment(data))
        
        db.session.add(test)
        db.session.commit()
        print('Hell Yeah ! It works')
        return redirect(url_for('home'))
    print('Working in it......')
    return render_template('test.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)