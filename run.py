from app import app
from app import db

if __name__ == '__main__':
    from app.database.models import Answer, Polls, User
    print(db)
    app.app_context().push()
    db.create_all()
    app.run(debug=True, host='0.0.0.0')