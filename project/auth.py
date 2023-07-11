from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db
from sqlalchemy.exc import IntegrityError

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    else:
        existing_user = User.query.filter_by(name=name).first()
        if existing_user:
            flash('Username already exists.')
            return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/update-profile')
@login_required
def update_profile():
    return render_template('update-profile.html')

@auth.route('/update-profile', methods=['POST'])
@login_required
def update_profile_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # Fetch the user from the database based on the authenticated user
    user = User.query.filter_by(email=email).first()

    # Perform necessary checks and update the user profile
    if user:
        # Check if the password meets the required criteria
        if password == user.password:
            flash('New password must be different from the current password.')
            return redirect(url_for('auth.update_profile'))

        # Check if the username is available
        if name != user.name:
            existing_user = User.query.filter_by(name=name).first()
            if existing_user:
                flash('Username already exists.')
                return redirect(url_for('auth.update_profile'))

        # Update the user profile in the database
        user.name = name
        user.password = password

        db.session.commit()
        return redirect(url_for('main.profile'))
    else:
        flash('Please enter correct email.')
        return redirect(url_for('auth.update_profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))