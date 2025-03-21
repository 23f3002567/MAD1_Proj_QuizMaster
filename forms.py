from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField

class loginForm():
    username = StringField(label='Username:')
    password = PasswordField(label='Password: ')

class registerForm():
    firstname=StringField(label = 'First Name:')
    lastname=StringField(label = 'Last Name:')
    qualification=StringField(label='Qualifications:')
    dob=DateField(label='Date of birth:')
    username = StringField(label='Username(email):')
    password = PasswordField(label='Password:')
    checkpwd= PasswordField(label='Enter password again:')