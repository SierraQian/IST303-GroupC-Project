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

def get_fred_data(indicator):
	fred_api_key = os.getenv('FRED_API_KEY', '8bf74e8cf0c1a4bfcde0f5db0436df43') # Create an environment variable after requesting your own FRED API key
	url = f"https://api.stlouisfed.org/fred/series/observations?series_id={indicator}&api_key={fred_api_key}&file_type=json"
	response = requests.get(url)
	data = response.json()
	latest_data_point = data['observations'][-1]['value']
	latest_data_point_date = data['observations'][-1]['date']
	return latest_data_point, latest_data_point_date

def dashboard():
	indicator_ids = ['GDPC1', 'CPIAUCSL', 'UNRATE', 'PAYEMS', 'A191RL1Q225SBEA', 'MORTGAGE30US', 'PSAVERT', 'FEDFUNDS', 'SP500', 'VIXCLS']
	fred_data = {indicator: get_fred_data(indicator) for indicator in indicator_ids}
	return fred_data

# def get_event_data():
#     fred_api_key = os.getenv('FRED_API_KEY', '8bf74e8cf0c1a4bfcde0f5db0436df43') # Create an environment variable after requesting your own FRED API key
#     indicator_ids = ['GDPC1', 'CPIAUCSL', 'UNRATE', 'PAYEMS', 'A191RL1Q225SBEA', 'MORTGAGE30US', 'PSAVERT', 'FEDFUNDS', 'SP500', 'VIXCLS']  # Replace with the actual series IDs for the indicators you're interested in
#     event_data = []

#     for indicator in indicator_ids:
#         url = f"https://api.stlouisfed.org/fred/series/observations?series_id={indicator}&api_key={fred_api_key}&file_type=json"
#         response = requests.get(url)
#         data = response.json()
#         latest_data_point = data['observations'][-1]

#         event_data.append({
#             'Date': latest_data_point['date'],
#             'Event': indicator,  # This is just the series ID. You might want to map this to a more descriptive event name.
#             'Country': 'USA',  # This is hardcoded. You might want to fetch this from somewhere if it varies.
#             'Previous': '',  # The FRED API doesn't provide this. You might need to fetch this from somewhere else.
#             'Forecast': '',  # The FRED API doesn't provide this. You might need to fetch this from somewhere else.
#             'Actual': latest_data_point['value'],
#         })

#     return event_data


@main.route('/profile')
@login_required
def profile():
	fred_data = dashboard()
	return render_template('profile.html', name=current_user.name, fred_data=fred_data)
