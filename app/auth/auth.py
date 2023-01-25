from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    from firebase_admin.auth import get_user_by_email, create_user
    from app import fb_app


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

            try:
                user = get_user_by_email(email, fb_app)

                flash('User with this email already exists.')

            except Exception as e:

                print(e)
                create_user(email= email, password = password_one)
                the_user = get_user_by_email(email)
                print(the_user)
            


    return render_template('signup.html')