from flask import Flask, Blueprint, render_template
from flask_login import login_required, current_user
from . import db
import requests
import os

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def index():
	fred_data = dashboard()
	return render_template('index.html', fred_data=fred_data)

# FRED API

def get_fred_data(indicator):
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
    
    return series_title, latest_data_point_value, latest_data_point_date, previous_data_point_value, previous_data_point_date


def dashboard():
	indicator_ids = ['GDPC1', 'CPIAUCSL', 'UNRATE', 'PAYEMS', 'A191RL1Q225SBEA', 'MORTGAGE30US', 'PSAVERT', 'FEDFUNDS', 'SP500', 'VIXCLS']
	fred_data = {indicator: get_fred_data(indicator) for indicator in indicator_ids}
	return fred_data

@main.route('/profile')
@login_required
def profile():
	fred_data = dashboard()
	return render_template('profile.html', name=current_user.name, fred_data=fred_data)
