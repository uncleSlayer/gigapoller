from flask import Flask
from app.auth.auth import auth
from app.api.api import api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# FLASK APP
app = Flask(__name__)

app.register_blueprint(api)
app.register_blueprint(auth)

app.secret_key = 'the only super secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://siddhant:sid00100@localhost:5432/gigapoller'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

bcrypt_app = Bcrypt(app)