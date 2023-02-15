from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    
    from app.database.models import User
    from app import bcrypt_app
    from app import db

    if request.method == 'POST':

        email = request.form.get('email')
        password_one = request.form.get('pass-one')
        password_two = request.form.get('pass-two')

        print(email, password_one, password_two)

        user = None

        if password_one != password_two:
            flash('Passwords do not match')

        if len(password_one) < 6:
            flash('Password must be minimum of 6 characters')
        
        else:


            user = User.query.filter_by(email=email).first()

            if user:

                flash('User with this email already exists.')
            else:

                password_hash = bcrypt_app.generate_password_hash(password=password_one).decode('utf-8')

                new_user = User(email = email, password_hash=password_hash)

                db.session.add(new_user)
                db.session.commit()

    return render_template('signup.html')


@auth.route('/login')
def login():

    return render_template('login.html')


@auth.route('/login-auth', methods=['POST'])
def login_auth():
    import jwt
    import datetime
    from app import app, bcrypt_app
    from flask import make_response
    from app.database.models import User
    from flask import redirect, flash

    login_data = request.get_json()


    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'sub': login_data['email']
    }

    jw_token = jwt.encode(
        payload,
        app.config.get('SECRET_KEY'),
        algorithm= 'HS256'
    )

    user_exist = User.query.filter_by(email= payload['sub']).first()

    print(user_exist)
    
    if user_exist:
        print(user_exist)

        user_exist_pass_hash = user_exist.password_hash
        if bcrypt_app.check_password_hash(user_exist_pass_hash, login_data['password']):
            resp = make_response()
            resp.set_cookie('access_token', jw_token, httponly= True, secure= True, samesite= 'strict')
            return resp
        
        else:
            flash('incorrect password given')

        
    else:
        flash('User with this email id does not exist')
        return redirect('login')
