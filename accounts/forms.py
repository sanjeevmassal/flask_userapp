from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app.extensions import db
from .models import User



class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=3)])
    last_name = StringField('First Name', validators=[])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def save_form(self):
        user = User(email=self.email.data,
             first_name=self.first_name.data,
             last_name=self.last_name.data,
             password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_user(self):
        user = User.query.filter_by(email=self.email.data).first()
        if user and user.check_password(self.password.data):
            return user
        return False
