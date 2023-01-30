from app import app
from app import db

if __name__ == '__main__':
    print(db)
    app.run(debug=True)