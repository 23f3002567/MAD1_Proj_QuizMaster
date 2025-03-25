from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class loginForm(FlaskForm):
    email = StringField(label='Username:', validators=[ DataRequired()])
    password = PasswordField(label='Password: ', validators=[Length(min=8, max=70), DataRequired()])
    submit=SubmitField(label='Submit')

class registerForm(FlaskForm):
    firstname=StringField(label = 'First Name:', validators=[Length(min=2, max=30), DataRequired()])
    lastname=StringField(label = 'Last Name:' ,validators=[Length(min=2, max=30), DataRequired()])
    qualification=StringField(label='Qualifications:', validators=[Length(min=2, max=300), DataRequired()])
    dob=DateField(label='Date of birth:', validators=[DataRequired()])
    email = StringField(label='Username(email):', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=8, max=70), DataRequired()])
    checkpwd= PasswordField(label='Enter password again:', validators=[EqualTo('password'), DataRequired()])
    submit= SubmitField(label='Submit')

class createSubForm(FlaskForm):
    subname=StringField(label='Subject Name:', validators=[Length(min=2, max=16), DataRequired()])
    subdesc=StringField(label='Description:', validators=[Length(min=2, max=500), DataRequired()])
    submit=SubmitField(label='Submit')

class createChpForm(FlaskForm):
    chpname=StringField(label='Chapter Name:', validators=[Length(min=2, max=16), DataRequired()])
    chpdesc=StringField(label='Description:', validators=[Length(min=2, max=500), DataRequired()])
    submit=SubmitField(label='Submit')
