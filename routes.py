from flask import render_template,redirect,url_for
from config import app,db
from models import User,Subject,Chapter,Quiz,Questions,Scores
from forms import registerForm,loginForm,createSubForm,createChpForm
from flask_login import login_user, logout_user, login_required,current_user



@app.route('/')
@login_required
def index():
    subject = Subject.query.all()
    return render_template("home.html",subject=subject)


@app.route('/register', methods=['POST','GET'])
def register():
    form=registerForm()
    if form.validate_on_submit() and not User.query.filter_by(email=form.email.data).first():
        newUser= User(name=form.firstname.data+" "+form.lastname.data,email=form.email.data,password=form.password.data,qualification=form.qualification.data,dob=form.dob.data)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template("register.html",form=form)


@app.route('/login', methods=['POST','GET'])
def login():
    form=loginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and user.password==form.password.data:
            login_user(user)
            return redirect(url_for('index'))
        
    return render_template("login.html", form=form)

@app.route('/logout', methods=['POST','GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/CreateSub', methods=['POST','GET'])
@login_required
def subcre():
    form=createSubForm()
    if form.validate_on_submit():
        newSub=Subject(name=form.subname.data,description=form.subdesc.data)
        db.session.add(newSub)
        db.session.commit()
        return redirect(url_for('index'))
    if current_user.email=="admin":
        return render_template("subcre.html",form=form)
    else:
        return redirect(url_for('index'))
    
@app.route('/deleteSub/<int:id>', methods=['POST','GET'])
@login_required
def subdel(id):
    if current_user.email=="admin":
        delsub=Subject.query.filter_by(id=id).first()
        db.session.delete(delsub)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    
@app.route('/subject/<sid>', methods=['POST','GET'])
@login_required
def chapters(sid): 
    subject=Subject.query.filter_by(id=sid).first()
    chapters=Chapter.query.filter_by(subject_id=sid).all()
    return render_template("chapters.html",subject=subject,chapters=chapters)

@app.route('/CreateChp/<sid>', methods=['POST','GET'])
@login_required
def chpcre(sid):
    form=createChpForm()
    if form.validate_on_submit():
        newChp=Chapter(name=form.chpname.data,description=form.chpdesc.data,subject_id=sid)
        db.session.add(newChp)
        db.session.commit()
        return redirect(url_for('chapters',sid=sid))
    if current_user.email=="admin":
        return render_template("chpcre.html",form=form)
    else:
        return redirect(url_for('index'))
    
@app.route('/deleteChp/<int:cid>', methods=['POST','GET'])
@login_required
def chpdel(cid):
    if current_user.email=="admin":
        delchp=Chapter.query.filter_by(id=cid).first()
        sid=delchp.subject_id
        db.session.delete(delchp)
        db.session.commit()
        return redirect(url_for('chapters', sid=sid))
    else:
        return redirect(url_for('index'))
    