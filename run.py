from flask import Flask
from app.extensions import db

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return 'here'

if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask_userapp'
    db.init_app(app)
    app.run(debug=True)