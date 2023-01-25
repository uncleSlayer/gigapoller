from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    from firebase_admin.auth import get_user_by_email
    from app import fb_app


    if request.method == 'POST':

        email = request.form.get('email')
        password_one = request.form.get('pass-one')
        password_two = request.form.get('pass-two')

        print(email, password_one, password_two)

        if password_one != password_two:
            flash('Passwords do not match')
        
        else:
            user = get_user_by_email(email, fb_app)
            print(user)


    return render_template('signup.html')