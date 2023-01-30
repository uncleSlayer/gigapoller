from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(250), unique = True)
    password_hash = db.Column(db.String(750), unique = True)