from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db=SQLAlchemy(app)


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