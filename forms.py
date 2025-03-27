from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField,SubmitField, RadioField
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

class createQuizForm(FlaskForm):
    quizname=StringField(label='Quiz Name:', validators=[Length(min=2, max=16), DataRequired()])
    date=DateField(label='Date of Quiz:', validators=[DataRequired()])
    time=StringField(label='Time Duration:', validators=[DataRequired()])
    remarks=StringField(label='Remarks:', validators=[Length(min=2, max=500), DataRequired()])
    submit=SubmitField(label='Submit')

class createQuesForm(FlaskForm):
    question_statement=StringField(label='Question:', validators=[Length(min=2, max=500), DataRequired()])
    correct_option=RadioField('Correct Option', choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')], validators=[DataRequired()])
    option1=StringField(label='Option 1:', validators=[Length(min=2, max=10), DataRequired()])
    option2=StringField(label='Option 2:', validators=[Length(min=2, max=10), DataRequired()])
    option3=StringField(label='Option 3:', validators=[Length(min=2, max=10), DataRequired()])
    option4=StringField(label='Option 4:', validators=[Length(min=2, max=10), DataRequired()])
    submit=SubmitField(label='Submit')
