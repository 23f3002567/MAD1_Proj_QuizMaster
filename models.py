from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user,UserMixin

login_manager=LoginManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db=SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) #check why user..get is not working

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(70), nullable=False)
    qualification = db.Column(db.String(300), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    scores = db.relationship('Scores', backref='usersuper', lazy=True)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    chapters = db.relationship('Chapter', backref='subjectsuper', lazy=True)

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    quizzes = db.relationship('Quiz', backref='chaptersuper', lazy=True)


class Quiz(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable=False)
    date_of_quiz = db.Column(db.DateTime, nullable=False)
    time_duration = db.Column(db.Integer, nullable=False)
    remarks = db.Column(db.String(500), nullable=False)
    questions = db.relationship('Questions', backref='quizsuper', lazy=True)

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    option1 = db.Column(db.String(10), nullable=False)
    option2 = db.Column(db.String(10), nullable=False)
    option3 = db.Column(db.String(10), nullable=False)
    option4 = db.Column(db.String(10), nullable=False)

#check relationships
class Scores(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    time_stamp_of_attempt = db.Column(db.DateTime, nullable=False)
    total_scored = db.Column(db.Integer, nullable=False)


with app.app_context():
    db.create_all()