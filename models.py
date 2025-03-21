from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(16), nullable=False)
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