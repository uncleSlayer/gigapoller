from flask import Flask
from app.auth.auth import auth
import firebase_admin
from firebase_admin import credentials, initialize_app

# FLASK APP
app = Flask(__name__)
app.register_blueprint(auth)
app.secret_key = 'the only super secret key'

# FIREBASE APP
cred = credentials.Certificate('app/fbcred.json')
fb_app = initialize_app(cred)

# FIREBASE AUTH APP