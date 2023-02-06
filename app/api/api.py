from flask import Blueprint, render_template, request

api = Blueprint('api', __name__)

@api.route('/home')
def home():
    from app import app
    import jwt

    token = request.cookies.get('access_token')
    print(token)

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

    

@api.route('/create-poll', methods= ['POST'])
def create_poll():

    from flask import jsonify
    from app import db
    from app.database.models import User
    from app.database.models import Polls
    import jwt

    poll_data = request.get_json()

    token = request.cookies.get('access_token')

    email_decoded = jwt.decode(token, 'the only super secret key', algorithms=['HS256'])

    email = email_decoded['sub']

    author = User.query.filter_by(email = email).first()
    print(poll_data['thirdAns'])

    poll = Polls(author= author.id, question= poll_data['question'], option_one= poll_data['firstAns'], option_two= poll_data['secondAns'], option_three= poll_data['thirdAns'], option_four= poll_data['fourthAns'], correct_answer= poll_data['correctAns'])
    db.session.add(poll)
    db.session.commit()

    return jsonify({
        'status': 'success' 
    }) 



@api.route('/share/<poll_id>')
def share_poll(poll_id):
    from app.database.models import User, Polls

    poll_details = Polls.query.filter_by(id= poll_id).first()

    print(poll_details)

    return render_template('share.html', poll_details= poll_details)