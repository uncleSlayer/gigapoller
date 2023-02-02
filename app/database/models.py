from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(250), unique = True)
    password_hash = db.Column(db.String(750), unique = True)
    polls = db.relationship('Polls', backref='author_user')



class Polls(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    question = db.Column(db.String(1000), nullable= False)
    option_one = db.Column(db.String(50), nullable= False)
    option_two = db.Column(db.String(50), nullable= False)
    option_three = db.Column(db.String(50), nullable= False)
    option_four = db.Column(db.String(50), nullable= False)
    correct_answer = db.Column(db.String(50), nullable= False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    