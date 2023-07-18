from flask import Flask, Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db
import requests, os

main = Blueprint('main', __name__)

# FRED API

def get_standard_data(indicator):
    fred_api_key = os.getenv('FRED_API_KEY', '8bf74e8cf0c1a4bfcde0f5db0436df43')
    url_series = f"https://api.stlouisfed.org/fred/series?series_id={indicator}&api_key={fred_api_key}&file_type=json" # Get an economic data series
    url_observations = f"https://api.stlouisfed.org/fred/series/observations?series_id={indicator}&api_key={fred_api_key}&file_type=json" # Get the observations or data values for an economic data series
    
    response_series = requests.get(url_series)
    data_series = response_series.json()
    
    try:
        series_title = data_series['seriess'][0]['title']
    except (KeyError, IndexError): # When the expected key is not found or when the list index is out of range, return N/A
        series_title = "N/A"
    
    response_observations = requests.get(url_observations)
    data_observations = response_observations.json()
    
    try:
        latest_data_point_value = data_observations['observations'][-1]['value']
        latest_data_point_date = data_observations['observations'][-1]['date']
    except (KeyError, IndexError): # When the expected key is not found or when the list index is out of range, return N/A
        latest_data_point_value = "N/A"
        latest_data_point_date = "N/A"
    
    try:
        previous_data_point_value = data_observations['observations'][-2]['value']
        previous_data_point_date = data_observations['observations'][-2]['date']
    except (KeyError, IndexError): # When the expected key is not found or when the list index is out of range, return N/A
        previous_data_point_value = "N/A"
        previous_data_point_date = "N/A"

    # Leverage float_to_money()
    
    try:
        latest_data_point_value = float_to_money(data_observations['observations'][-1]['value'])
        latest_data_point_date = data_observations['observations'][-1]['date']
    except (KeyError, IndexError): 
        latest_data_point_value = "N/A"
        latest_data_point_date = "N/A"
    
    try:
        previous_data_point_value = float_to_money(data_observations['observations'][-2]['value'])
        previous_data_point_date = data_observations['observations'][-2]['date']
    except (KeyError, IndexError): 
        previous_data_point_value = "N/A"
        previous_data_point_date = "N/A"
    
    return series_title, latest_data_point_value, latest_data_point_date, previous_data_point_value, previous_data_point_date


def get_standard_data_dashboard():
        indicator_ids = ['GDPC1', 'CPIAUCSL', 'UNRATE', 'PAYEMS', 'A191RL1Q225SBEA', 'MORTGAGE30US', 'PSAVERT', 'FEDFUNDS', 'SP500', 'VIXCLS']
        standard_data = {indicator: get_standard_data(indicator) for indicator in indicator_ids}
        return standard_data
    
def customized_dashboard(indicator_ids, standard_data):
    if not indicator_ids:
        return standard_data
    else:
        return {indicator: get_standard_data(indicator) for indicator in indicator_ids}
        
# Convert Integers into a readable format (Money)
        
def float_to_money(amount, currency_symbol="$"):
    try:
        amount = float(amount)
        return f"{currency_symbol}{amount:,.2f}"
    except ValueError:  # raised when trying to convert a string that doesn't represent a number
        return amount


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