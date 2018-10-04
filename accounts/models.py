# https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one
from flask_user import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db,  login_manager

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0', default=False)
    password_hash = db.Column(db.String(255), nullable=False, server_default='')
    last_login = db.Column(db.DateTime)
    is_admin = db.Column(db.Boolean, default=False)
    create_date = db.Column(db.DateTime, default=db.func.now())

    
    @property
    def password(self):
        raise AttributeError('Password is not readable attribute.')
    
    @password.setter
    def password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User: {}>'.format(self.email)
    
    @login_manager.user_loader
    def load_user(self,user_id):
        return User.query.get(int(user_id))