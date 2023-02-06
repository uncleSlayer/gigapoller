from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(250), unique = True)
    password_hash = db.Column(db.String(750), unique = True)
    polls = db.relationship('Polls', backref='author_user')
    answer = db.relationship('Answer', backref= 'poll_author')



class Polls(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    question = db.Column(db.String(1000), nullable= False)
    option_one = db.Column(db.String(50), nullable= False)
    option_two = db.Column(db.String(50), nullable= False)
    option_three = db.Column(db.String(50), nullable= False)
    option_four = db.Column(db.String(50), nullable= False)
    correct_answer = db.Column(db.String(50), nullable= False)
    answerer = db.relationship('Answer', backref= 'poll')


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'))
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    answer = db.Column(db.String(50), nullable= False)
    

    