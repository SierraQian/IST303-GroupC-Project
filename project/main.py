from flask import Flask, Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db
from .fred import get_standard_data, get_standard_data_dashboard, customized_dashboard, float_to_money

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def index():
    standard_data = get_standard_data_dashboard()
    return render_template('index.html', standard_data=standard_data)

@main.route('/profile', methods=['GET', 'POST'])  # Allow both GET and POST requests
@login_required
def profile():
    standard_data = get_standard_data_dashboard()
    if request.method == 'POST':  # If the route is accessed via POST request (i.e., the form was submitted)
        indicator_ids = request.form.getlist('indicator_ids')  # Get the selected indicator IDs from the POST data
        customized_data = customized_dashboard(indicator_ids, standard_data)  # Generate the customized data
    else:  # If the route is accessed via GET request
        customized_data = standard_data  # Use the standard data
    return render_template('profile.html', name=current_user.name, customized_data=customized_data)


@main.route('/indicator-form')
@login_required
def indicator_form():
    return render_template('indicators-form.html')