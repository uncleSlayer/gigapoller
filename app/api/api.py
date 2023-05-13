from flask import Blueprint, render_template, request

api = Blueprint('api', __name__)

# home page
# ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++
@api.route('/home')
def home():
    from app import app
    import jwt
    from app.database.models import Polls, User

    token = request.cookies.get('access_token')
    print(token)

    try:
        payload = jwt.decode(
        token,
        app.config.get('SECRET_KEY'),
        algorithms=["HS256"]
        )
        print(payload)

        current_user = User.query.filter_by(email=payload['sub']).first()

        polls = Polls.query.filter_by(author= current_user.id).all()
        print(polls)

        return render_template('home.html', payload = payload, polls= polls)

    except jwt.ExpiredSignatureError:
        print('Signature expired. Please login again.')
    except jwt.InvalidTokenError:
        print('Invalid token. Please login again')

    return render_template('login.html')

    

# poll creation api
# ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++
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

    return jsonify(
        {
            "message": "success"
        }
    )




# share poll api
# ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++
@api.route('/share/<poll_id>', methods= ['GET'])
def share_poll(poll_id):
    from app.database.models import Polls

    poll_details = Polls.query.filter_by(id= poll_id).first()

    print(poll_details)

    return render_template('share.html', poll_details= poll_details)




# vote api
# ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++
@api.route('/share/vote', methods= ['POST'])
def vote():
    import jwt
    from app.database.models import Answer, Polls, User
    from app import app, db
    from flask import flash
    
    token = request.cookies.get('access_token')
    vote = request.get_json()
    print(vote)
    token_decoded = jwt.decode(
        token,
        app.config.get('SECRET_KEY'),
        algorithms=["HS256"]
    )
    current_user = User.query.filter_by(email= token_decoded['sub']).first()

    question = vote['question']
    answer = vote['answer']
    poll = Polls.query.filter_by(question= question).first()

    if Answer.query.filter_by(poll_id= poll.id, author= current_user.id).first():
        print('You have already voted for this poll')

    else:
        answer = Answer(poll_id= poll.id, author= current_user.id, answer= answer)
        db.session.add(answer)
        db.session.commit()
    
    print(token_decoded)

    print(current_user)

    return 'success'



# poll details page
# ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++++
@api.route('/details/<pollid>')
def poll_details(pollid):
    from app.database.models import Answer, Polls

    poll = Polls.query.filter_by(id= pollid).first()

    answers = Answer.query.filter_by(poll_id= poll.id).all()

    print(answers)

    answers_count = len(answers)

    option_one_count = 0
    option_two_count = 0
    option_three_count = 0
    option_four_count = 0

    for answer in answers:
        if answer.answer == poll.option_one:
            option_one_count += 1
        
        elif answer.answer == poll.option_two:
            option_two_count += 1

        elif answer.answer == poll.option_three:
            option_three_count += 1 
        
        elif answer.answer == poll.option_four:
            option_four_count += 1

    
    result = {
        'question': poll.question,
        'options': [
            {
                'option_name': poll.option_one,
                'vote_percentage': (option_one_count / answers_count) * 100
            },
            {
                'option_name': poll.option_two,
                'vote_percentage': (option_two_count / answers_count) * 100
            },
            {
                'option_name': poll.option_three,
                'vote_percentage': (option_three_count / answers_count) * 100
            },
            {
                'option_name': poll.option_four,
                'vote_percentage': (option_four_count / answers_count) * 100
            }
        ]
    }

    print(result)

    return render_template('polldetails.html', result= result)
