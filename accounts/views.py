from .forms import LoginForm, RegistrationForm
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from . import account
from .models import User
from app.extensions import db


@account.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        form.save_form()
        flash('You have successfully registered! You may now login.')
        return redirect(url_for('accounts.login'))
    return render_template('auth/register.html', form=form, title='Register')


@account.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = form.validate_user()
        if user :
            login_user(user)
            return redirect(url_for('home.dashboard'))
        else:
            flash('Invalid email or password.')
    return render_template('auth/login.html', form=form, title='Login')


@account.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('accounts.login'))