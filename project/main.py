from flask import Flask, Blueprint, render_template, request, session, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .fred import get_standard_data, get_standard_data_dashboard, customized_dashboard
from .models import User
from werkzeug.security import generate_password_hash

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def index():
    standard_data = get_standard_data_dashboard()
    title = "Home"
    return render_template('index.html', standard_data=standard_data, title=title)


@main.route('/profile', methods=['GET', 'POST'])  # Allow both GET and POST requests
@login_required
def profile():
    standard_data = get_standard_data_dashboard()
    user = User.query.filter_by(email=current_user.email).first()  # Fetch the current user from the database
    title = "Profile"

    if request.method == 'POST':  # If the route is accessed via POST request (i.e., the form was submitted)
        indicator_ids = request.form.getlist('indicator_ids')  # Get the selected indicator IDs from the POST data
        customized_data = customized_dashboard(indicator_ids, standard_data)  # Generate the customized data
        selected_indicators_string = ','.join(indicator_ids) # Convert list to string
        user.indicators = selected_indicators_string # Update the user's indicators
        db.session.commit() # Commit changes to the database
    else:  # If the route is accessed via GET request
        # Check if user has already saved indicators
        if user.indicators:
            indicator_ids = user.indicators.split(',')  # Get the saved indicator IDs from the user
            customized_data = customized_dashboard(indicator_ids, standard_data)  # Generate the customized data
        else:
            customized_data = standard_data  # Use the standard data
    
    return render_template('profile.html', name=current_user.name, customized_data=customized_data, current_user=current_user, title=title)  


@main.route('/update-profile', methods=['POST'])
@login_required
def update_profile():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(email=current_user.email).first() # Fetch the current user from the database
    title = "Update Profile"

    # update fields
    user.email = email
    user.name = name
    if password:  # Only update the password if a new one was provided
        user.password = generate_password_hash(password, method='sha256')

    db.session.commit()  # save changes to the database

    flash('Your profile was successfully updated.', 'success')
    return redirect(url_for('main.profile'), title=title)  # Redirect back to profile page


@main.route('/indicator-form')
@login_required
def indicator_form():
    title = "Indicator Form"
    return render_template('indicators-form.html', title=title)
    
