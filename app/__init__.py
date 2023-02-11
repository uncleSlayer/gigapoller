from flask import Flask
from app.auth.auth import auth
from app.api.api import api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

# FLASK APP
app = Flask(__name__)

app.register_blueprint(api)
app.register_blueprint(auth)

app.secret_key = 'the only super secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

bcrypt_app = Bcrypt(app)