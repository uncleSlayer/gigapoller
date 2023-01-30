from flask import Blueprint, render_template

api = Blueprint('api', __name__)

@api.route('/home/<token>')
def home(token):
    from app import app
    import jwt

    try:
        payload = jwt.decode(
        token,
        app.config.get('SECRET_KEY'),
        algorithms=["HS256"]
        )
        print(payload)
        return render_template('home.html', payload = payload)

    except jwt.ExpiredSignatureError:
        print('Signature expired. Please login again.')
    except jwt.InvalidTokenError:
        print('Invalid token. Please login again')

    return render_template('login.html')

    