from app import app
from flask import render_template,redirect,url_for
import models
from forms import registerForm,loginForm
from flask_login import login_user


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/register', methods=['POST','GET'])
def register():
    form=registerForm()
    if form.validate_on_submit():
        newUser= models.User(name=form.firstname.data+" "+form.lastname.data,email=form.email.data,password=form.password.data,qualification=form.qualification.data,dob=form.dob.data)
        models.db.session.add(newUser)
        models.db.session.commit()
        return redirect(url_for('login'))
    
    return render_template("register.html",form=form)


@app.route('/login', methods=['POST','GET'])
def login():
    form=loginForm()
    if form.validate_on_submit():
        user=models.User.query.filter_by(email=form.email.data).first()
        if user and user.password==form.password.data:
            login_user(user)
            return redirect(url_for('index'))
        
    return render_template("login.html", form=form)